#!/usr/bin/env python3
"""
🎭 Voice Shapeshifter - Simplified TTS Demo
Używa edge-tts dla łatwej instalacji i szybkiego startu!
"""

import asyncio
import edge_tts
import pygame
import os
import tempfile
from pathlib import Path

# Lista dostępnych głosów
VOICES = {
    "PL-Marek": "pl-PL-MarekNeural",
    "PL-Zofia": "pl-PL-ZofiaNeural", 
    "EN-Guy": "en-US-GuyNeural",
    "EN-Jenny": "en-US-JennyNeural",
    "EN-Aria": "en-US-AriaNeural",
    "FR-Henri": "fr-FR-HenriNeural",
    "DE-Conrad": "de-DE-ConradNeural",
    "ES-Alvaro": "es-ES-AlvaroNeural",
    "IT-Diego": "it-IT-DiegoNeural",
    "JP-Nanami": "ja-JP-NanamiNeural",
    "KR-SunHi": "ko-KR-SunHiNeural",
    "CN-Xiaoxiao": "zh-CN-XiaoxiaoNeural"
}

# Style mówienia
STYLES = {
    "normal": "",
    "cheerful": "style='cheerful'",
    "sad": "style='sad'",
    "angry": "style='angry'",
    "excited": "style='excited'",
    "friendly": "style='friendly'",
    "hopeful": "style='hopeful'",
    "shouting": "style='shouting'",
    "whispering": "style='whispering'",
    "terrified": "style='terrified'",
    "unfriendly": "style='unfriendly'"
}

async def text_to_speech(text, voice, style="normal", rate="+0%", pitch="+0Hz"):
    """Konwertuj tekst na mowę z różnymi parametrami"""
    
    # Przygotuj SSML jeśli styl jest wybrany
    if style != "normal" and STYLES[style]:
        ssml_text = f"<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>"
        ssml_text += f"<voice name='{voice}'>"
        ssml_text += f"<prosody rate='{rate}' pitch='{pitch}'>"
        ssml_text += f"<mstts:express-as {STYLES[style]}>{text}</mstts:express-as>"
        ssml_text += "</prosody></voice></speak>"
        communicate = edge_tts.Communicate(ssml_text, voice)
    else:
        # Zwykły tekst z parametrami
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    
    # Zapisz do pliku tymczasowego
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_path = tmp_file.name
        
    await communicate.save(tmp_path)
    return tmp_path

def play_audio(file_path):
    """Odtwórz plik audio"""
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Czekaj aż skończy grać
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Usuń plik tymczasowy
    os.unlink(file_path)

async def demo():
    """Główne demo"""
    print("🎭 VOICE SHAPESHIFTER - Edge TTS Demo")
    print("=" * 50)
    print("\n📢 Dostępne głosy:")
    
    for name, voice_id in VOICES.items():
        print(f"  • {name}: {voice_id}")
    
    print("\n🎨 Dostępne style:")
    for style in STYLES.keys():
        print(f"  • {style}")
    
    print("\n" + "=" * 50)
    
    # Demo 1: Różne głosy
    print("\n🎤 DEMO 1: Różne głosy mówiące to samo")
    text = "Cześć! Jestem Voice Shapeshifter. Potrafię mówić różnymi głosami!"
    
    for name, voice in list(VOICES.items())[:4]:  # Pierwsze 4 głosy
        print(f"\n  → Głos: {name}")
        audio_file = await text_to_speech(text, voice)
        print(f"  ✅ Wygenerowano: {name}.mp3")
        # play_audio(audio_file)  # Odkomentuj żeby odsłuchać
    
    # Demo 2: Różne emocje
    print("\n\n🎭 DEMO 2: Ten sam głos, różne emocje")
    voice = VOICES["EN-Jenny"]
    text = "This is amazing! I can speak with different emotions!"
    
    for style in ["normal", "cheerful", "sad", "excited", "whispering"]:
        print(f"\n  → Styl: {style}")
        audio_file = await text_to_speech(text, voice, style=style)
        print(f"  ✅ Wygenerowano: {style}.mp3")
        # play_audio(audio_file)  # Odkomentuj żeby odsłuchać
    
    # Demo 3: Pitch i prędkość
    print("\n\n🔧 DEMO 3: Modyfikacja głosu (pitch & speed)")
    voice = VOICES["PL-Marek"]
    text = "Mogę mówić wysoko, nisko, szybko lub wolno!"
    
    variations = [
        ("normalny", "+0%", "+0Hz"),
        ("szybki", "+50%", "+0Hz"),
        ("wolny", "-30%", "+0Hz"),
        ("wysoki", "+0%", "+5Hz"),
        ("niski", "+0%", "-5Hz"),
        ("chipmunk", "+30%", "+8Hz"),
        ("demon", "-20%", "-8Hz")
    ]
    
    for name, rate, pitch in variations:
        print(f"\n  → Wariacja: {name} (rate={rate}, pitch={pitch})")
        audio_file = await text_to_speech(text, voice, rate=rate, pitch=pitch)
        print(f"  ✅ Wygenerowano: {name}.mp3")
        # play_audio(audio_file)  # Odkomentuj żeby odsłuchać
    
    # Demo 4: Multi-language
    print("\n\n🌍 DEMO 4: Wielojęzyczność")
    
    multilang = [
        ("Polski", VOICES["PL-Zofia"], "Witaj świecie! To jest niesamowite!"),
        ("English", VOICES["EN-Guy"], "Hello world! This is amazing!"),
        ("Français", VOICES["FR-Henri"], "Bonjour le monde! C'est incroyable!"),
        ("Deutsch", VOICES["DE-Conrad"], "Hallo Welt! Das ist unglaublich!"),
        ("日本語", VOICES["JP-Nanami"], "こんにちは世界！これは素晴らしいです！")
    ]
    
    for lang, voice, text in multilang:
        print(f"\n  → {lang}: {text}")
        audio_file = await text_to_speech(text, voice)
        print(f"  ✅ Wygenerowano: {lang}.mp3")
        # play_audio(audio_file)  # Odkomentuj żeby odsłuchać
    
    print("\n\n✨ Demo zakończone!")
    print("💡 Odkomentuj play_audio() w kodzie żeby odsłuchać wygenerowane pliki")

async def interactive_mode():
    """Tryb interaktywny"""
    print("\n🎮 TRYB INTERAKTYWNY")
    print("=" * 50)
    
    while True:
        print("\n📝 Wpisz tekst (lub 'quit' żeby wyjść):")
        text = input("> ")
        
        if text.lower() == 'quit':
            break
            
        print("\n🎤 Wybierz głos:")
        for i, (name, _) in enumerate(VOICES.items()):
            print(f"  {i+1}. {name}")
        
        try:
            choice = int(input("> ")) - 1
            voice_name = list(VOICES.keys())[choice]
            voice = VOICES[voice_name]
        except:
            print("❌ Nieprawidłowy wybór, używam domyślnego")
            voice = VOICES["PL-Marek"]
        
        print("\n🎨 Wybierz styl (Enter dla normalnego):")
        for style in STYLES.keys():
            print(f"  • {style}")
        
        style_choice = input("> ").strip() or "normal"
        if style_choice not in STYLES:
            style_choice = "normal"
        
        print("\n⏳ Generuję...")
        audio_file = await text_to_speech(text, voice, style=style_choice)
        print("✅ Gotowe! Odtwarzam...")
        
        play_audio(audio_file)

if __name__ == "__main__":
    print("🎭 VOICE SHAPESHIFTER - Simplified Edition")
    print("Używa Edge-TTS dla łatwej instalacji!")
    print("\nWybierz tryb:")
    print("1. Demo automatyczne")
    print("2. Tryb interaktywny")
    
    choice = input("\nWybór (1/2): ")
    
    if choice == "2":
        asyncio.run(interactive_mode())
    else:
        asyncio.run(demo())