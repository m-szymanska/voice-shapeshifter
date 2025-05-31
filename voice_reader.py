#!/usr/bin/env python3
"""
🎭 Voice Reader - Czyta dowolny tekst dowolnym głosem!
"""

import asyncio
import edge_tts
import pygame
import sys
from pathlib import Path

# Wszystkie dostępne głosy
VOICES = {
    "1": ("pl-PL-MarekNeural", "🇵🇱 Marek (Polski męski)"),
    "2": ("pl-PL-ZofiaNeural", "🇵🇱 Zofia (Polski żeński)"),
    "3": ("en-US-GuyNeural", "🇺🇸 Guy (Angielski męski)"),
    "4": ("en-US-JennyNeural", "🇺🇸 Jenny (Angielski żeński)"),
    "5": ("en-US-AriaNeural", "🇺🇸 Aria (Angielski naturalny)"),
    "6": ("fr-FR-HenriNeural", "🇫🇷 Henri (Francuski)"),
    "7": ("de-DE-ConradNeural", "🇩🇪 Conrad (Niemiecki)"),
    "8": ("es-ES-AlvaroNeural", "🇪🇸 Alvaro (Hiszpański)"),
    "9": ("it-IT-DiegoNeural", "🇮🇹 Diego (Włoski)"),
    "10": ("ja-JP-NanamiNeural", "🇯🇵 Nanami (Japoński)"),
    "11": ("ko-KR-SunHiNeural", "🇰🇷 SunHi (Koreański)"),
    "12": ("zh-CN-XiaoxiaoNeural", "🇨🇳 Xiaoxiao (Chiński)"),
}

# Style mówienia (dla niektórych głosów)
STYLES = {
    "1": ("normalny", "+0%", "+0Hz"),
    "2": ("szybki", "+30%", "+0Hz"),
    "3": ("wolny", "-20%", "+0Hz"),
    "4": ("wysoki", "+0%", "+5Hz"),
    "5": ("niski", "+0%", "-5Hz"),
    "6": ("robot", "-10%", "-8Hz"),
    "7": ("chipmunk", "+40%", "+10Hz"),
    "8": ("senny", "-30%", "-3Hz"),
    "9": ("podekscytowany", "+20%", "+3Hz"),
}

async def text_to_speech(text, voice, rate="+0%", pitch="+0Hz"):
    """Konwertuj tekst na mowę"""
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    output_path = "temp_output.mp3"
    await communicate.save(output_path)
    return output_path

def play_audio(file_path):
    """Odtwórz plik audio"""
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    print("\n▶️  Odtwarzanie... (naciśnij Ctrl+C aby przerwać)")
    try:
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\n⏹️  Zatrzymano odtwarzanie")
    
    # Usuń plik tymczasowy
    Path(file_path).unlink(missing_ok=True)

async def main():
    print("🎭 VOICE READER - Czytaj teksty różnymi głosami!")
    print("=" * 60)
    
    # Pobierz tekst
    print("\n📝 KROK 1: Wpisz lub wklej tekst do przeczytania:")
    print("(Możesz używać wielu linii. Zakończ pustą linią)")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    text = "\n".join(lines)
    if not text:
        print("❌ Nie podano tekstu!")
        return
    
    print(f"\n✅ Tekst ({len(text)} znaków) zapisany!")
    
    # Wybierz głos
    print("\n🎤 KROK 2: Wybierz głos:")
    for key, (voice_id, name) in VOICES.items():
        print(f"  {key:>2}. {name}")
    
    voice_choice = input("\nWybór (1-12): ").strip()
    if voice_choice not in VOICES:
        print("❌ Nieprawidłowy wybór, używam domyślnego (Marek)")
        voice_choice = "1"
    
    voice_id, voice_name = VOICES[voice_choice]
    print(f"✅ Wybrany głos: {voice_name}")
    
    # Wybierz styl
    print("\n🎨 KROK 3: Wybierz styl mówienia:")
    for key, (style_name, rate, pitch) in STYLES.items():
        print(f"  {key}. {style_name}")
    
    style_choice = input("\nWybór (1-9): ").strip()
    if style_choice not in STYLES:
        style_choice = "1"
    
    style_name, rate, pitch = STYLES[style_choice]
    print(f"✅ Wybrany styl: {style_name}")
    
    # Generuj
    print("\n⏳ Generuję audio...")
    try:
        audio_file = await text_to_speech(text, voice_id, rate, pitch)
        print("✅ Audio wygenerowane!")
        
        # Opcja zapisu
        save = input("\n💾 Czy zapisać plik? (t/n): ").lower()
        if save == 't':
            filename = input("Nazwa pliku (bez .mp3): ").strip() or "output"
            save_path = f"{filename}.mp3"
            Path(audio_file).rename(save_path)
            print(f"✅ Zapisano jako: {save_path}")
            audio_file = save_path
        
        # Odtwórz
        play_audio(audio_file)
        
    except Exception as e:
        print(f"❌ Błąd: {e}")
    
    # Ponownie?
    again = input("\n🔄 Przeczytać coś jeszcze? (t/n): ").lower()
    if again == 't':
        await main()

if __name__ == "__main__":
    print("🚀 Uruchamiam Voice Reader...")
    print("💡 Wskazówka: Możesz wkleić długie teksty!")
    print("💡 Wskazówka: Różne głosy lepiej czytają w swoich językach")
    print("")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Do zobaczenia!")
    except Exception as e:
        print(f"\n❌ Błąd: {e}")