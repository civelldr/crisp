# CRISP

CRISP is a tiny Python script that uses the power of Spotify to make you a playlist based on the artists you specify. Currently, it's exploring some darkwave, but make it your own.

I only use OSX, so I can't guarantee it'll work on Windows or Linux.
## What You Need to Get Going

1. **Spotify Developer Account** - You'll need this to get your API keys.
2. **Python & some packages** - Specifically, `spotipy`.

## How to Set Up

1. Go to the Spotify Developer Dashboard, create an app, and get your keys.
2. Add these keys to your `.zshrc` or `.bashrc` as environment variables.
   
   ```
   export SPOTIPY_CLIENT_ID='your-spotify-client-id'
   export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
   export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
   ```

    PS: Use http://localhost:8080/callback as the redirect URI. The first time you run the script, a browser window will pop up asking you to log in to Spotify. Just a heads-up!

3. After adding them, source your .zshrc or .bashrc.

## Running CRISP

`python3 CRISP.py`

When you first run it will pop open a window asking you to log in to Spotify.
Once it's done, pop over to Spotify and your new playlist is waiting for you.