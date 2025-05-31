# 🎭 Voice Shapeshifter

> **Transform any text into speech with multiple voices, emotions, and styles!**

A fun voice synthesis project created during a late-night coding session with Claude AI and Monica. Uses Microsoft Edge's neural TTS engine to create various voice effects and personalities.

## ✨ Features

- 🌍 **12+ Neural Voices** - Polish, English, French, German, Spanish, Italian, Japanese, Korean, Chinese
- 🎭 **Multiple Styles** - Normal, Robot, Chipmunk, Sleepy, Excited, Whisper
- 🎨 **Voice Effects** - Adjust speed and pitch for unique characters
- 📝 **Text-to-Speech** - Convert any text to natural-sounding speech
- 🎵 **Batch Generation** - Create multiple variations at once
- 💾 **Export to MP3** - Save your creations

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/yourusername/voice-shapeshifter.git
cd voice-shapeshifter

# Setup (one time only)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install edge-tts pygame

# Run demos
python generate_demo_voices.py    # Generate sample voices
python voice_reader.py           # Interactive text reader
python simple_tts_demo.py        # Full demo with all features
```

## 🎯 Usage Examples

### Generate a simple greeting
```python
python demo_claude_monica.py
```
This creates 6 variations of "Cześć, jestem głosem który powstał dzięki Claude i Monice!"

### Read any text with any voice
```bash
python voice_reader.py
# Then follow the prompts to:
# 1. Enter your text
# 2. Choose a voice (1-12)
# 3. Choose a style (1-9)
# 4. Listen and optionally save
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

## 🙏 Credits

Created with ❤️ during a fun coding session between:
- **Claude** (Anthropic's AI assistant)
- **Monica** (The human with crazy ideas)

Special thanks to Microsoft for the amazing Edge TTS engine!

---

*"Cześć, jestem głosem który powstał dzięki Claude i Monice, witam serdecznie!"* 🎭