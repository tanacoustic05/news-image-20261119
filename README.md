# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/tanacoustic05/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/tanacoustic05/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

The image sums up 19 November 2026's world news in a single frame: the trilateral summit handshake between the US, Chinese and Russian presidents in the APEC hall in Shenzhen, under golden light and three national flags. The repository ships that image, and `main.py` writes it to `/output/entry.png` offline and deterministically — a byte-for-byte copy with no network access and no rendering step.

## Run

```sh
python main.py
```

The entry ships as bundled_entry.png (1024x1024, JPEG, under 1 MiB); main.py copies it byte-for-byte into $MAKEFUN_OUTPUT_DIR (default ./output) with no network access, using only the standard library.
