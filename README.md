# Home Assistot

A Home Assistant dashboard for my toddler daughter.

## Development

```bash
pip install -r requirements.txt
```

```bash
export LONG_LIVED_ACCESS_KEY=your_access_key
export SERVER_URL=http://your.home.assistant:8123
python app.py
```

## Docker

### Build

```bash
docker build -t home-assistot .
```

### Run

```bash
docker run -d \
  --name home-assistant-home-assistot \
  --restart=always \
  -p 5000:5000 \
  -e LONG_LIVED_ACCESS_KEY=your_access_key \
  -e SERVER_URL=http://your.home.assistant:8123 \
  home-assistot
```
