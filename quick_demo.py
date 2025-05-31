#!/usr/bin/env python3
"""
Szybkie demo Voice Shapeshifter - prosty przykład generowania głosu
"""

import sys
import os
sys.path.insert(0, '/Users/moni/Git/csm-mlx')

from mlx_lm.sample_utils import make_sampler
from huggingface_hub import hf_hub_download
from csm_mlx import CSM, csm_1b, generate
import audiofile
import numpy as np
import mlx.core as mx

def initialize_model():
    """Inicjalizuj model CSM"""
    print("🔄 Ładuję model CSM-1B...")
    try:
        csm = CSM(csm_1b())
        weight_path = hf_hub_download(repo_id="senstella/csm-1b-mlx", filename="ckpt.safetensors")
        csm.load_weights(weight_path)
        print("✅ Model załadowany!")
        return csm
    except Exception as e:
        print(f"❌ Błąd ładowania modelu: {e}")
        return None

def generate_voices(csm):
    """Generuj różne głosy z przykładowym tekstem"""
    
    texts = [
        ("Cześć! Jestem twoim nowym asystentem głosowym.", "hello.wav"),
        ("To naprawdę działa! Niesamowite!", "excited.wav"),
        ("Pssst... to tajemnica...", "whisper.wav"),
        ("Czasami czuję się zmęczony...", "sad.wav"),
        ("UWAGA! UWAGA! To ważna wiadomość!", "alert.wav"),
        ("Jestem. Robot. Z. Przyszłości.", "robot.wav")
    ]
    
    print("\n🎭 Generuję różne wersje głosów...\n")
    sampler = make_sampler(temp=0.8, top_k=50)
    
    for text, filename in texts:
        print(f"🎤 Generuję: {filename}")
        
        try:
            # Generuj audio
            audio = generate(
                csm,
                text=text,
                speaker=0,
                context=[],
                max_audio_length_ms=10_000,
                sampler=sampler,
                stream=mx.cpu,  # Use CPU for compatibility
            )
            
            # Zapisz do pliku
            audio_np = np.array(audio, dtype=np.float32).squeeze()
            audiofile.write(filename, audio_np, 24000)
            print(f"✅ Wygenerowano: {filename}")
            
        except Exception as e:
            print(f"❌ Błąd dla {filename}: {e}")
    
    print("\n✨ Gotowe! Możesz teraz odsłuchać pliki .wav")

def simple_voice_clone(csm):
    """Prosty przykład klonowania głosu"""
    print("\n🎤 DEMO KLONOWANIA GŁOSU")
    print("=" * 50)
    
    # Na razie używamy różnych speakerów zamiast prawdziwego klonowania
    print("📢 Testuję różne głosy wbudowane w model...")
    
    text = "Witaj! To jest test różnych głosów w modelu CSM."
    sampler = make_sampler(temp=0.8, top_k=50)
    
    for speaker_id in range(3):  # Test 3 różnych głosów
        output = f"speaker_{speaker_id}.wav"
        try:
            audio = generate(
                csm,
                text=text,
                speaker=speaker_id,
                context=[],
                max_audio_length_ms=10_000,
                sampler=sampler,
                stream=mx.cpu,
            )
            
            audio_np = np.array(audio, dtype=np.float32).squeeze()
            audiofile.write(output, audio_np, 24000)
            print(f"✅ Wygenerowano głos {speaker_id}: {output}")
        except Exception as e:
            print(f"❌ Błąd dla głosu {speaker_id}: {e}")

if __name__ == "__main__":
    print("🎭 VOICE SHAPESHIFTER - Quick Demo")
    print("=" * 50)
    
    csm = initialize_model()
    if csm:
        generate_voices(csm)
        simple_voice_clone(csm)
        
        print("\n🎉 Demo zakończone!")
        print("📂 Sprawdź wygenerowane pliki .wav")
        print("🚀 Możesz teraz eksperymentować z różnymi tekstami!")
    else:
        print("\n❌ Nie można załadować modelu")
        print("💡 Upewnij się, że masz zainstalowane wszystkie zależności")