#!/usr/bin/env python3
"""
🌐 Voice Shapeshifter Web App
Prosta aplikacja webowa do zabawy głosami!
"""

import gradio as gr
import asyncio
import edge_tts
from pathlib import Path
import tempfile
import random

# Import naszych szalonych modów
from crazy_modes import CrazyVoiceModes

# Głosy
VOICES = {
    "🇵🇱 Marek (Polski)": "pl-PL-MarekNeural",
    "🇵🇱 Zofia (Polska)": "pl-PL-ZofiaNeural",
    "🇺🇸 Guy (English)": "en-US-GuyNeural",
    "🇺🇸 Jenny (English)": "en-US-JennyNeural",
    "🇫🇷 Henri (Français)": "fr-FR-HenriNeural",
    "🇩🇪 Conrad (Deutsch)": "de-DE-ConradNeural",
    "🇪🇸 Alvaro (Español)": "es-ES-AlvaroNeural",
    "🇯🇵 Nanami (日本語)": "ja-JP-NanamiNeural",
}

# Style - EKSTREMALNE różnice!
STYLES = {
    "🎯 Normalny": ("+0%", "+0Hz"),
    "🤖 Robot": ("-25%", "-12Hz"),  # Bardziej mechaniczny
    "🐿️ Wiewiórka": ("+80%", "+20Hz"),  # MEGA wysoki i szybki
    "😴 Senny": ("-50%", "-5Hz"),  # Bardzo wolny i niski
    "🎉 Podekscytowany": ("+40%", "+8Hz"),  # Szybki i wysoki
    "🤫 Szept": ("-60%", "-8Hz"),  # Super cichy i niski
    "👹 Gigant": ("-40%", "-20Hz"),  # MEGA niski i wolny
    "⚡ Turbo": ("+100%", "+5Hz"),  # ULTRA szybki
    "😈 Demon": ("-50%", "-25Hz"),  # ULTRA niski i wolny
    "🎪 Klaun": ("+30%", "+12Hz"),  # Wesoły i wysoki
    "🥶 Zmrożony": ("-15%", "+10Hz"),  # Drżący z zimna
    "👶 Dziecko": ("+50%", "+25Hz"),  # Bardzo wysoki
    "🤠 Kowboj": ("-10%", "-8Hz"),  # Niski i pewny siebie
    "🎤 Raper": ("+15%", "-5Hz"),  # Szybki ale niski
}

async def generate_voice(text, voice_name, style_name):
    """Generuj głos"""
    voice = VOICES[voice_name]
    rate, pitch = STYLES[style_name]
    
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_path = tmp_file.name
    
    await communicate.save(tmp_path)
    return tmp_path

async def generate_drunk_mode(text):
    """Drunk mode dla web"""
    crazy = CrazyVoiceModes()
    
    # Użyj polskiego głosu
    files = await crazy.drunk_mode(text, "pl_male")
    
    # Zwróć ostatni (najbardziej pijany) plik
    if files:
        return files[-1]
    return None

async def generate_reverse_psychology(text):
    """Reverse psychology dla web"""
    crazy = CrazyVoiceModes()
    
    # Wykryj język
    lang = "pl" if any(word in text.lower() for word in ["cześć", "kocham", "lubię", "świetnie"]) else "en"
    
    files = await crazy.reverse_psychology_mode(text, lang)
    
    # Zwróć oba pliki
    if len(files) >= 2:
        return files[0], files[1]  # happy ironic, sad truth
    return None, None

# Przykładowe teksty
EXAMPLES = [
    "Cześć! Jestem Voice Shapeshifter. Potrafię mówić różnymi głosami!",
    "Hello! I can speak in many different voices and styles. Try me!",
    "Kocham poniedziałki! To mój ulubiony dzień tygodnia!",
    "I love Mondays! They're absolutely amazing!",
    "Dzisiaj pokażę wam jak działa synteza mowy. To fascynujące!",
]

# Gradio interface
with gr.Blocks(title="🎭 Voice Shapeshifter", theme=gr.themes.Soft()) as app:
    gr.Markdown("""
    # 🎭 Voice Shapeshifter Web App
    
    **Baw się głosami! Stwórz robota, wiewiórka, albo upij swój głos!** 
    
    Projekt stworzony przez Claude AI i Monikę podczas szalonej nocnej sesji kodowania 🌙
    """)
    
    with gr.Tab("🎯 Podstawowy Generator"):
        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(
                    label="Tekst do przeczytania",
                    placeholder="Wpisz dowolny tekst...",
                    lines=3
                )
                voice_dropdown = gr.Dropdown(
                    choices=list(VOICES.keys()),
                    value="🇵🇱 Marek (Polski)",
                    label="Wybierz głos"
                )
                style_dropdown = gr.Dropdown(
                    choices=list(STYLES.keys()),
                    value="🎯 Normalny",
                    label="Wybierz styl"
                )
                generate_btn = gr.Button("🎤 Generuj głos!", variant="primary")
            
            with gr.Column():
                audio_output = gr.Audio(label="Wygenerowany głos", type="filepath")
                
        gr.Examples(
            examples=EXAMPLES[:3],
            inputs=text_input
        )
    
    with gr.Tab("🍺 Drunk Mode"):
        gr.Markdown("""
        ### 🍺 Tryb Pijany - głos stopniowo się upija!
        
        Wpisz długi tekst i obserwuj jak głos przechodzi od trzeźwego do totalnie pijanego!
        """)
        
        drunk_text = gr.Textbox(
            label="Tekst (im dłuższy, tym lepszy efekt!)",
            placeholder="Wpisz długi tekst, który będzie czytany coraz bardziej pijackim głosem...",
            lines=5,
            value="Dzień dobry państwu! Dzisiaj opowiem wam o fascynującej technologii syntezy mowy. Na początku wszystko jest jasne i klarowne. Ale z czasem zaczynam czuć się coraz bardziej rozluźniony. Może to przez tę technologię? A może to coś innego? Już nie wiem co mówię. Wszystko się kręci!"
        )
        drunk_btn = gr.Button("🍻 Upij głos!", variant="primary")
        drunk_audio = gr.Audio(label="Najbardziej pijany fragment", type="filepath")
        drunk_status = gr.Markdown("*Kliknij przycisk aby rozpocząć upijanie głosu...*")
    
    with gr.Tab("🔄 Reverse Psychology"):
        gr.Markdown("""
        ### 🔄 Tryb Odwrotnej Psychologii
        
        Mówi coś, ale myśli dokładnie odwrotnie! Generuje dwie wersje:
        - 😊 **Ironicznie szczęśliwa** - udaje że wszystko super
        - 😢 **Prawdziwie smutna** - mówi co naprawdę myśli
        """)
        
        reverse_text = gr.Textbox(
            label="Tekst z pozytywnymi słowami",
            placeholder="np. 'Kocham poniedziałki! Świetnie się czuję!'",
            lines=3,
            value="Kocham poniedziałki! To mój ulubiony dzień tygodnia. Świetnie się czuję i jestem bardzo szczęśliwy!"
        )
        reverse_btn = gr.Button("🎭 Generuj przeciwieństwa!", variant="primary")
        
        with gr.Row():
            reverse_happy = gr.Audio(label="😊 Wersja ironicznie szczęśliwa", type="filepath")
            reverse_sad = gr.Audio(label="😢 Wersja prawdziwie smutna", type="filepath")
    
    with gr.Tab("🎲 Losowy Szał"):
        gr.Markdown("""
        ### 🎲 Nie wiesz co wybrać? Kliknij i się przekonaj!
        """)
        
        random_text = gr.Textbox(
            label="Tekst",
            value="Cześć! To jest test losowego głosu i stylu!",
            lines=2
        )
        random_btn = gr.Button("🎰 Losuj wszystko!", variant="primary")
        random_audio = gr.Audio(label="Losowa kombinacja", type="filepath")
        random_info = gr.Markdown("")
    
    # Funkcje
    def sync_generate(text, voice, style):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            return loop.run_until_complete(generate_voice(text, voice, style))
        finally:
            loop.close()
    
    def sync_drunk(text):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(generate_drunk_mode(text))
            return result, "🍺 Głos został upity! Od trzeźwego do totalnie pijanego!"
        finally:
            loop.close()
    
    def sync_reverse(text):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            happy, sad = loop.run_until_complete(generate_reverse_psychology(text))
            return happy, sad
        finally:
            loop.close()
    
    def random_generate(text):
        voice = random.choice(list(VOICES.keys()))
        style = random.choice(list(STYLES.keys()))
        audio = sync_generate(text, voice, style)
        info = f"**Wylosowano:** {voice} w stylu {style}"
        return audio, info
    
    # Podłącz akcje
    generate_btn.click(
        sync_generate,
        inputs=[text_input, voice_dropdown, style_dropdown],
        outputs=audio_output
    )
    
    drunk_btn.click(
        sync_drunk,
        inputs=drunk_text,
        outputs=[drunk_audio, drunk_status]
    )
    
    reverse_btn.click(
        sync_reverse,
        inputs=reverse_text,
        outputs=[reverse_happy, reverse_sad]
    )
    
    random_btn.click(
        random_generate,
        inputs=random_text,
        outputs=[random_audio, random_info]
    )
    
    gr.Markdown("""
    ---
    
    ### 🛠️ Informacje techniczne
    - Używa Microsoft Edge TTS (darmowe, wysokiej jakości)
    - Nie wymaga API key ani rejestracji
    - Działa na każdym systemie z Pythonem
    
    ### 🎯 Wskazówki
    - Polskie głosy najlepiej czytają polski tekst
    - Drunk Mode działa najlepiej z długimi tekstami
    - Reverse Psychology wykrywa słowa pozytywne i zamienia na negatywne
    
    ### 💙 Credits
    Stworzone z miłością przez **Claude** (AI) i **Monikę** (człowiek) podczas spontanicznej sesji kodowania!
    
    Kod źródłowy: https://github.com/m-szymanska/voice-shapeshifter
    
    *"Cześć, jestem głosem który powstał dzięki Claude i Monice!"* 🎭
    """)

if __name__ == "__main__":
    print("🚀 Uruchamiam Voice Shapeshifter Web App...")
    print("📢 Otwórz przeglądarkę i wejdź na podany adres!")
    print("💡 Możesz też udostępnić aplikację publicznie klikając 'Share'")
    
    # Utwórz folder output jeśli nie istnieje
    Path("output").mkdir(exist_ok=True)
    
    # Uruchom aplikację
    app.launch(
        share=False,  # Zmień na True aby udostępnić publicznie
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True  # Automatycznie otwórz przeglądarkę
    )