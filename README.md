# 📺 HLS Proxy Worker

A Cloudflare Worker that helps you **fetch and rewrite HLS (`.m3u8`) playlists**.
It is useful when IPTV or streaming links **don’t play directly**, because some providers require special headers like **Origin** and **Referer**.

With this worker you can:

* Proxy `.m3u8` playlists through Cloudflare.
* Automatically rewrite relative paths into full URLs.
* Add custom headers (Origin, Referer, User-Agent) when needed.
* Use it for IPTV, testing, or custom media apps.

---

## 🚀 What You Need

* A **free Cloudflare account** (includes **100,000 requests per day**).
* (Optional) [Reqable](https://reqable.com/) – to capture request headers.

---

## 🔧 Setup Instructions (No Wrangler Needed)

1. Sign in to [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Go to **Workers & Pages → Create Application → Create Worker**.
3. Delete the default code and **copy-paste the contents of `index.js` from this repo**.
4. Click **Deploy**.

Your worker will be live at something like:

```
https://hls-proxy-worker.username.workers.dev/?url=YOUR_M3U8_LINK
```

---

## 🎯 Usage

Pass a `url` query parameter:

```
https://your-worker-domain/?url=https://example.com/live/playlist.m3u8
```

The worker will return a valid `.m3u8` file you can open in **VLC, IPTV players, or media apps**.

---

## 🔒 When Do You Need Origin & Referer?

Some streaming providers **block direct requests** unless they come from a specific website.
Example: a stream only works when opened on `example.com`, but fails in your IPTV app.

That’s when you add a **rule** in the worker:

```js
const rules = {
    "example.com": {
        Origin: "https://example.com",
        Referer: "https://example.com/",
    },
};
```

With this, your worker will send the correct headers and bypass the restriction.

---

## 🕵️ How to Find Headers with Reqable

If you don’t know which headers are needed:

1. Install [Reqable](https://reqable.com/).
2. Open the stream in your browser or app while Reqable is running.
3. Find the request to the `.m3u8` file.
4. Look at the **Request Headers**.

   * If you see `Origin` or `Referer`, copy them.
5. Add them to the `rules` in your worker.

Example from Reqable:

```
Origin: https://example.com
Referer: https://example.com/
```

Paste these into your worker code.

---

## 📌 Notes

* Free Cloudflare Workers have **100,000 requests/day**.
* For higher limits, upgrade to a paid plan.
* This project is for **educational & personal use**.

---

## ⭐ Support

If you find this project useful, please **give it a star** ⭐ on GitHub — it helps others discover it and keeps the project alive.

Please respect the streaming providers’ terms of service.