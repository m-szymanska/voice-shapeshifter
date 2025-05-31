#!/usr/bin/env python3
"""
🎭 Voice Shapeshifter - Zmień swój głos w dowolny inny!
Używa CSM-MLX do klonowania i transformacji głosu w czasie rzeczywistym.
"""

import gradio as gr
import numpy as np
import soundfile as sf
import tempfile
import os
from pathlib import Path
import subprocess
import json

class VoiceShapeshifter:
    def __init__(self):
        self.voice_samples = {}
        self.temp_dir = Path(tempfile.mkdtemp())
        
    def record_voice_sample(self, name, audio_path):
        """Nagraj próbkę głosu do klonowania"""
        if audio_path is None:
            return "❌ Nagraj próbkę głosu!"
        
        # Zapisz próbkę
        self.voice_samples[name] = audio_path
        return f"✅ Zapisano głos '{name}'! Teraz możesz go używać do transformacji."
    
    def transform_voice(self, text, source_voice, target_voice, emotion="neutral"):
        """Transformuj tekst używając wybranego głosu"""
        if target_voice not in self.voice_samples:
            return None, "❌ Najpierw nagraj głos docelowy!"
        
        # Przygotuj ścieżkę wyjściową
        output_path = self.temp_dir / f"output_{len(os.listdir(self.temp_dir))}.wav"
        
        # Dodaj emocje do tekstu
        emotion_prompts = {
            "neutral": text,
            "happy": f"[laughs] {text} [happy]",
            "sad": f"[sighs] {text} [sad]",
            "angry": f"{text}! [angry]",
            "excited": f"{text}!!! [excited]",
            "whisper": f"[whispers] {text}",
            "robot": f"[robotic] {text} [beep]"
        }
        
        enhanced_text = emotion_prompts.get(emotion, text)
        
        # Użyj CSM-MLX do generacji
        cmd = [
            "csm-mlx", "generate",
            enhanced_text,
            "--voice", self.voice_samples[target_voice],
            "-o", str(output_path)
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if result.returncode == 0 and output_path.exists():
                return str(output_path), f"✅ Transformacja udana! Użyto głosu: {target_voice}"
            else:
                return None, f"❌ Błąd: {result.stderr}"
        except Exception as e:
            return None, f"❌ Błąd: {str(e)}"
    
    def mix_voices(self, text, voice1, voice2, mix_ratio=0.5):
        """Miksuj dwa głosy razem"""
        # To wymaga bardziej zaawansowanej implementacji
        # Na razie używamy prostego przełączania
        if mix_ratio < 0.5:
            return self.transform_voice(text, "default", voice1)
        else:
            return self.transform_voice(text, "default", voice2)

# Inicjalizacja
shapeshifter = VoiceShapeshifter()

# Interfejs Gradio
with gr.Blocks(title="🎭 Voice Shapeshifter", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🎭 Voice Shapeshifter
    
    Zmień swój głos w dowolny inny! Nagraj próbki głosów i używaj ich do transformacji.
    
    ## 🎯 Instrukcja:
    1. Nagraj próbki różnych głosów (swój, znajomych, z filmów)
    2. Wpisz tekst do wypowiedzenia
    3. Wybierz głos docelowy i emocję
    4. Kliknij "Transformuj" i słuchaj magii!
    """)
    
    with gr.Tab("🎤 Nagrywanie Głosów"):
        with gr.Row():
            voice_name = gr.Textbox(label="Nazwa głosu", placeholder="np. 'Mój głos', 'Robot', 'Smerf'")
            audio_recorder = gr.Audio(source="microphone", type="filepath", label="Nagraj próbkę (3-10 sekund)")
        
        record_btn = gr.Button("💾 Zapisz próbkę głosu", variant="primary")
        record_status = gr.Textbox(label="Status", interactive=False)
        
    with gr.Tab("🔄 Transformacja"):
        text_input = gr.Textbox(
            label="Tekst do wypowiedzenia",
            placeholder="Wpisz co ma powiedzieć AI...",
            lines=3
        )
        
        with gr.Row():
            source_voice = gr.Dropdown(
                choices=["default"] + list(shapeshifter.voice_samples.keys()),
                value="default",
                label="Głos źródłowy"
            )
            target_voice = gr.Dropdown(
                choices=list(shapeshifter.voice_samples.keys()),
                label="Głos docelowy"
            )
            emotion = gr.Radio(
                choices=["neutral", "happy", "sad", "angry", "excited", "whisper", "robot"],
                value="neutral",
                label="Emocja"
            )
        
        transform_btn = gr.Button("🎭 Transformuj głos!", variant="primary")
        
        audio_output = gr.Audio(label="Wygenerowany głos", type="filepath")
        transform_status = gr.Textbox(label="Status", interactive=False)
    
    with gr.Tab("🎨 Eksperymentalne"):
        gr.Markdown("### 🧪 Miksowanie głosów (wkrótce!)")
        with gr.Row():
            voice_mix_1 = gr.Dropdown(choices=list(shapeshifter.voice_samples.keys()), label="Głos 1")
            voice_mix_2 = gr.Dropdown(choices=list(shapeshifter.voice_samples.keys()), label="Głos 2")
            mix_slider = gr.Slider(0, 1, 0.5, label="Proporcja miksowania")
        
        gr.Markdown("### 🎭 Przykładowe transformacje")
        gr.Examples(
            examples=[
                ["Cześć, jestem robotem z przyszłości!", "robot"],
                ["Pssst... to tajemnica...", "whisper"],
                ["Hurra! Wygraliśmy!", "excited"],
                ["Och, to smutne...", "sad"]
            ],
            inputs=[text_input, emotion]
        )
    
    # Akcje
    record_btn.click(
        shapeshifter.record_voice_sample,
        inputs=[voice_name, audio_recorder],
        outputs=[record_status]
    ).then(
        lambda: gr.Dropdown.update(choices=list(shapeshifter.voice_samples.keys())),
        outputs=[target_voice]
    )
    
    transform_btn.click(
        shapeshifter.transform_voice,
        inputs=[text_input, source_voice, target_voice, emotion],
        outputs=[audio_output, transform_status]
    )

if __name__ == "__main__":
    print("🎭 Uruchamiam Voice Shapeshifter...")
    print("📢 Upewnij się, że masz zainstalowane csm-mlx!")
    demo.launch(share=True)