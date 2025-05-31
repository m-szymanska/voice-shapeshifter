# 🎭 Voice Shapeshifter

> **Zmień tekst w głos z szalonymi efektami! Pijany głos, robot, wiewiórka i więcej!**

Projekt stworzony podczas nocnej sesji kodowania z Claude AI i Moniką. Używa darmowego Microsoft Edge TTS do tworzenia różnych efektów głosowych.

## 🎬 ZOBACZ DEMO (kliknij obrazek)
[![Voice Shapeshifter Demo](https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
*(wkrótce prawdziwe demo!)*

## ✨ Features

- 🌍 **12+ Neural Voices** - Polish, English, French, German, Spanish, Italian, Japanese, Korean, Chinese
- 🎭 **Multiple Styles** - Normal, Robot, Chipmunk, Sleepy, Excited, Whisper
- 🎨 **Voice Effects** - Adjust speed and pitch for unique characters
- 📝 **Text-to-Speech** - Convert any text to natural-sounding speech
- 🎵 **Batch Generation** - Create multiple variations at once
- 💾 **Export to MP3** - Save your creations

## 🚀 JAK URUCHOMIĆ (dla totalnych początkujących!)

### Krok 1: Sprawdź czy masz Pythona
Otwórz terminal (Mac/Linux) lub Command Prompt (Windows) i wpisz:
```bash
python --version
```
Jeśli nie masz, pobierz z [python.org](https://python.org) (wybierz wersję 3.8 lub nowszą)

### Krok 2: Pobierz projekt
```bash
# Opcja A: Jeśli masz git
git clone https://github.com/m-szymanska/voice-shapeshifter.git

# Opcja B: Jeśli NIE masz git - po prostu:
# 1. Kliknij zielony przycisk "Code" na stronie projektu
# 2. Wybierz "Download ZIP"
# 3. Rozpakuj gdzie chcesz
```

### Krok 3: Wejdź do folderu projektu
```bash
cd voice-shapeshifter
```

### Krok 4: Zainstaluj wszystko (tylko raz!)
```bash
# Windows:
python -m venv venv
venv\Scripts\activate
pip install -r requirements_simple.txt

# Mac/Linux:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_simple.txt
```

### Krok 5: URUCHOM APLIKACJĘ! 🎉
```bash
python web_app.py
```

**Otworzy się przeglądarka z aplikacją na http://localhost:7860**

### 🆘 Jeśli coś nie działa:

**Problem: "python nie jest rozpoznawane"**
- Zainstaluj Python z python.org
- Na Windows: podczas instalacji zaznacz "Add Python to PATH"

**Problem: "No module named 'edge_tts'"**
- Upewnij się że aktywowałeś venv (powinno być (venv) na początku linii)
- Spróbuj: `pip install edge-tts pygame gradio`

**Problem: "Port 7860 zajęty"**
- Zamknij inne aplikacje lub zmień port w web_app.py

## 🎯 JAK UŻYWAĆ APLIKACJI

### Po uruchomieniu web_app.py:

1. **🎯 Podstawowy Generator**
   - Wpisz dowolny tekst
   - Wybierz głos (np. Marek, Zofia)
   - Wybierz styl (np. Robot, Wiewiórka)
   - Kliknij "Generuj głos!"

2. **🍺 Drunk Mode (Tryb Pijany)**
   - Wpisz długi tekst
   - Kliknij "Upij głos!"
   - Głos stopniowo się upija od trzeźwego do totalnie pijanego!

3. **🔄 Reverse Psychology**
   - Wpisz tekst z pozytywnymi słowami (np. "Kocham poniedziałki!")
   - Dostaniesz 2 wersje:
     - Ironicznie szczęśliwą 😊
     - Prawdziwie smutną 😢

4. **🎲 Losowy Szał**
   - Kliknij "Losuj wszystko!"
   - Aplikacja wybierze losowy głos i styl

### Inne skrypty (dla zaawansowanych):
```bash
# Wygeneruj przykładowe głosy
python generate_demo_voices.py

# Interaktywny czytacz tekstów
python voice_reader.py

# Testuj szalone tryby
python crazy_modes.py
```

### Available Voices

| Language | Voice Name | Description |
|----------|------------|-------------|
| 🇵🇱 Polish | Marek | Male voice |
| 🇵🇱 Polish | Zofia | Female voice |
| 🇺🇸 English | Guy | Male voice |
| 🇺🇸 English | Jenny | Female voice |
| 🇺🇸 English | Aria | Natural voice |
| 🇫🇷 French | Henri | Male voice |
| 🇩🇪 German | Conrad | Male voice |
| 🇪🇸 Spanish | Alvaro | Male voice |
| 🇮🇹 Italian | Diego | Male voice |
| 🇯🇵 Japanese | Nanami | Female voice |
| 🇰🇷 Korean | SunHi | Female voice |
| 🇨🇳 Chinese | Xiaoxiao | Female voice |

### Voice Styles

- 🎯 **Normal** - Default voice
- 🤖 **Robot** - Mechanical, deep voice
- 🐿️ **Chipmunk** - High-pitched, fast
- 😴 **Sleepy** - Slow, low energy
- 🎉 **Excited** - Fast, high energy
- 🤫 **Whisper** - Quiet, mysterious
- 👹 **Giant** - Deep, slow, imposing
- And more!

## 🛠️ Project Structure

```
voice-shapeshifter/
├── output/                  # Generated audio files
├── simple_tts_demo.py      # Main demo with all features
├── voice_reader.py         # Interactive text-to-speech
├── generate_demo_voices.py # Batch voice generation
├── demo_claude_monica.py   # Special greeting demo
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🎨 Examples

Check out the `output/` folder after running the demos:
- `pl_marek_robot.mp3` - Polish robot voice
- `en_jenny_happy.mp3` - Happy English voice
- `en_guy_chipmunk.mp3` - Chipmunk effect
- `ja_nanami.mp3` - Japanese voice
- And many more!

## 🔧 Requirements

- Python 3.8+
- No special hardware needed
- Works on Windows, macOS, Linux
- Internet connection (for TTS API)

## 📝 Notes

- Uses Microsoft Edge's Text-to-Speech service
- High-quality neural voices
- No API key required
- Completely free to use

## 🚀 Future Ideas

- [ ] Real-time voice transformation
- [ ] GUI with Gradio/Streamlit
- [ ] Voice mixing (combine multiple voices)
- [ ] Emotion detection and auto-styling
- [ ] Podcast/audiobook generator
- [ ] Voice effects (echo, reverb)

## 🤝 Contributing

Feel free to fork, modify, and create pull requests! Some ideas:
- Add more voice effects
- Create a web interface
- Add more languages
- Implement voice cloning

## 📜 License

MIT License - Use it however you want!

## 🤔 FAQ (Często Zadawane Pytania)

**P: Czy to jest darmowe?**
O: TAK! 100% darmowe. Edge TTS nie wymaga żadnych opłat ani API key.

**P: Czy mogę użyć wygenerowanych głosów komercyjnie?**
O: Sprawdź warunki użytkowania Microsoft Edge TTS. Kod projektu jest na licencji MIT.

**P: Dlaczego niektóre głosy źle czytają polski tekst?**
O: Używaj polskich głosów (Marek, Zofia) dla polskiego tekstu. Angielskie głosy nie znają polskiej wymowy.

**P: Mogę dodać własny głos?**
O: Edge TTS nie obsługuje klonowania głosu. Możesz tylko wybierać z dostępnych głosów.

**P: Działa offline?**
O: NIE. Edge TTS wymaga połączenia z internetem.

**P: Mogę to uruchomić na telefonie?**
O: Teoretycznie tak (jeśli masz Python na telefonie), ale łatwiej użyć na komputerze.

## 🙏 Credits

Created with ❤️ during a fun coding session between:
- **Claude** (Anthropic's AI assistant) 
- **Monika** (The human with crazy ideas)

Special thanks to Microsoft for the amazing Edge TTS engine!

---

*"Cześć, jestem głosem który powstał dzięki Claude i Monice, witam serdecznie!"* 🎭

**⭐ Jeśli podoba Ci się projekt, zostaw gwiazdkę na GitHubie! ⭐**