#!/usr/bin/env python3
"""
🤪 CRAZY MODES - Szalone tryby głosowe!
Drunk Mode & Reverse Psychology
"""

import asyncio
import edge_tts
import random
import re
from pathlib import Path

class CrazyVoiceModes:
    def __init__(self):
        self.voices = {
            "pl_male": "pl-PL-MarekNeural",
            "pl_female": "pl-PL-ZofiaNeural",
            "en_male": "en-US-GuyNeural",
            "en_female": "en-US-JennyNeural"
        }
    
    async def drunk_mode(self, text, voice="pl_male"):
        """
        🍺 DRUNK MODE - Głos się upija z każdym słowem!
        """
        print("\n🍺 DRUNK MODE ACTIVATED!")
        print("=" * 50)
        
        words = text.split()
        drunk_levels = [
            # (rate, pitch, opis)
            ("+0%", "+0Hz", "Trzeźwy"),
            ("-5%", "-1Hz", "Pierwsze piwo"),
            ("-10%", "-2Hz", "Drugie piwo"),
            ("-15%", "+1Hz", "Trzecie piwo..."),
            ("-20%", "-3Hz", "Czwarte... hik!"),
            ("-25%", "+2Hz", "Piąte... wszystko się kręci"),
            ("-30%", "-4Hz", "Szóste... kto wyłączył grawitację?"),
            ("-35%", "+3Hz", "Siódme... kocham wszystkich!"),
            ("-40%", "-5Hz", "Ósme... *bełkot*"),
        ]
        
        output_files = []
        
        # Dzielimy tekst na części i każda jest bardziej pijana
        chunk_size = max(1, len(words) // len(drunk_levels))
        
        for i, (rate, pitch, desc) in enumerate(drunk_levels):
            start = i * chunk_size
            end = start + chunk_size if i < len(drunk_levels) - 1 else len(words)
            chunk = " ".join(words[start:end])
            
            if not chunk:
                continue
                
            # Dodaj losowe "hik!" i bełkot
            if i >= 3:
                chunk = self._add_drunk_effects(chunk, i)
            
            print(f"\n🥴 Level {i+1}: {desc}")
            print(f"   Tekst: {chunk}")
            
            communicate = edge_tts.Communicate(
                chunk, 
                self.voices[voice],
                rate=rate,
                pitch=pitch
            )
            
            filename = f"output/drunk_level_{i+1}.mp3"
            await communicate.save(filename)
            output_files.append(filename)
            print(f"   ✅ Zapisano: {filename}")
        
        print("\n🍻 Drunk progression complete!")
        return output_files
    
    def _add_drunk_effects(self, text, drunk_level):
        """Dodaje pijackie efekty do tekstu"""
        effects = [
            " *hik* ",
            " eee... ",
            " yyyy... ",
            " czekaj... ",
            " o kurde... ",
            " hehe... ",
            " *burp* "
        ]
        
        words = text.split()
        result = []
        
        for word in words:
            result.append(word)
            # Im bardziej pijany, tym więcej efektów
            if random.random() < (drunk_level * 0.15):
                result.append(random.choice(effects))
        
        return " ".join(result)
    
    async def reverse_psychology_mode(self, text, language="pl"):
        """
        🔄 REVERSE PSYCHOLOGY - Mówi odwrotnie niż myśli!
        """
        print("\n🔄 REVERSE PSYCHOLOGY MODE!")
        print("=" * 50)
        
        # Słownik przeciwieństw
        opposites = {
            # Polski
            "kocham": ("nienawidzę", "sad"),
            "lubię": ("nie znoszę", "angry"),
            "super": ("okropne", "disgusted"),
            "świetnie": ("tragicznie", "sad"),
            "piękny": ("brzydki", "disappointed"),
            "dobry": ("zły", "angry"),
            "wesoły": ("smutny", "sad"),
            "szczęśliwy": ("nieszczęśliwy", "depressed"),
            # English
            "love": ("hate", "angry"),
            "like": ("despise", "disgusted"),
            "great": ("terrible", "sad"),
            "happy": ("miserable", "depressed"),
            "beautiful": ("ugly", "disappointed"),
            "good": ("bad", "angry"),
            "awesome": ("awful", "sad"),
            "amazing": ("horrible", "disgusted")
        }
        
        # Analiza tekstu i podmiana
        words = text.lower().split()
        transformed_words = []
        emotions = []
        
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word)
            if clean_word in opposites:
                opposite, emotion = opposites[clean_word]
                transformed_words.append(word.replace(clean_word, opposite))
                emotions.append(emotion)
            else:
                transformed_words.append(word)
        
        reversed_text = " ".join(transformed_words)
        
        # Wybierz głos i emocję
        if language == "pl":
            voice = self.voices["pl_female"]
            # Sarkastyczny ton
            rate = "-10%"
            pitch = "-2Hz"
        else:
            voice = self.voices["en_female"]
            rate = "-15%"
            pitch = "-3Hz"
        
        print(f"\n😇 Oryginalny tekst: {text}")
        print(f"😈 Reverse psychology: {reversed_text}")
        print(f"🎭 Emocje wykryte: {', '.join(set(emotions)) if emotions else 'brak'}")
        
        # Generuj dwie wersje
        output_files = []
        
        # 1. Wesoła wersja oryginału (ironicznie)
        print("\n📢 Generuję wersję 'szczęśliwą' (ironiczną)...")
        communicate1 = edge_tts.Communicate(
            text,
            voice,
            rate="+20%",
            pitch="+5Hz"
        )
        filename1 = "output/reverse_psych_happy_ironic.mp3"
        await communicate1.save(filename1)
        output_files.append(filename1)
        print(f"✅ {filename1}")
        
        # 2. Smutna wersja przeciwieństwa
        print("\n📢 Generuję wersję 'prawdziwą' (smutną)...")
        communicate2 = edge_tts.Communicate(
            reversed_text,
            voice,
            rate=rate,
            pitch=pitch
        )
        filename2 = "output/reverse_psych_sad_truth.mp3"
        await communicate2.save(filename2)
        output_files.append(filename2)
        print(f"✅ {filename2}")
        
        return output_files

async def demo():
    """Demo szalonych trybów"""
    crazy = CrazyVoiceModes()
    
    # DRUNK MODE
    drunk_text = "Cześć wszystkim! Dzisiaj pokażę wam jak działa synteza mowy. To naprawdę fascynujące! Możemy kontrolować każdy aspekt głosu."
    await crazy.drunk_mode(drunk_text)
    
    # REVERSE PSYCHOLOGY
    reverse_texts = [
        "Kocham poniedziałki! To mój ulubiony dzień tygodnia. Świetnie się czuję!",
        "I love Mondays! They're absolutely amazing and I feel great!"
    ]
    
    for text, lang in zip(reverse_texts, ["pl", "en"]):
        await crazy.reverse_psychology_mode(text, lang)
    
    print("\n\n🎉 SZALONE TRYBY WYGENEROWANE!")
    print("\n🎧 Odsłuchaj pliki w folderze output/")
    print("   - drunk_level_*.mp3 - progresja upicia")
    print("   - reverse_psych_*.mp3 - ironiczne wersje")

async def interactive():
    """Tryb interaktywny"""
    crazy = CrazyVoiceModes()
    
    print("\n🤪 CRAZY VOICE MODES - Tryb interaktywny")
    print("=" * 50)
    
    while True:
        print("\n🎯 Wybierz tryb:")
        print("1. 🍺 Drunk Mode")
        print("2. 🔄 Reverse Psychology")
        print("3. 🚪 Wyjście")
        
        choice = input("\nWybór (1-3): ")
        
        if choice == "3":
            break
        
        text = input("\n📝 Wpisz tekst: ")
        
        if choice == "1":
            lang = input("Język (pl/en): ") or "pl"
            voice = f"{lang}_male"
            await crazy.drunk_mode(text, voice)
        elif choice == "2":
            lang = input("Język (pl/en): ") or "pl"
            await crazy.reverse_psychology_mode(text, lang)
        
        print("\n✅ Gotowe! Sprawdź folder output/")

if __name__ == "__main__":
    import sys
    
    print("🤪 CRAZY VOICE MODES")
    print("Drunk Mode & Reverse Psychology!")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        asyncio.run(interactive())
    else:
        asyncio.run(demo())