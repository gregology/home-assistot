# Home Assistot

A simple Home Assistant dashboard for my toddler daughter.

![image](https://github.com/gregology/home-assistot/assets/1595448/b700b6fd-827c-4c77-98d4-e4df609584ac)

Right or left clicking the mouse on each section triggers a script with the corresponding name in Home Assistant.

![image](https://github.com/gregology/home-assistot/assets/1595448/63759525-7746-42e5-8d3b-d1a15f1664a3)

## Development

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run app with environment variables

```bash
export LONG_LIVED_ACCESS_KEY=your_access_key
export SERVER_URL=http://your.home.assistant:8123
python app.py
```

Note: `LONG_LIVED_ACCESS_KEY` can be created using the "Long-Lived Access Tokens" section at the bottom of a user's Home Assistant profile page. 

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
