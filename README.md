# emaki Chocolatey package

Chocolatey package for the official [emaki](https://emaki.ai/?utm_source=chocolatey&utm_medium=package) CLI. emaki is the Japanese-language AI video generator for [Seedance 2.5](https://emaki.ai/seedance-2-5) and [Seedance 2.0](https://emaki.ai/seedance-2).

```
choco install emaki
emaki -credits
emaki "a paper lantern drifting over a night river"
```

Set `EMAKI_API_KEY` to a key from https://emaki.ai/settings/apikeys. Runs cost credits on your emaki account, the same price as on the website.

`tools/emaki.exe` is the `emaki-windows-amd64.exe` asset of [emaki-go v0.1.0](https://github.com/hanshs474/emaki-go/releases/tag/v0.1.0); see `tools/VERIFICATION.txt`. Also on the web: [image to video](https://emaki.ai/image-to-video) and the [AI video upscaler](https://emaki.ai/video-upscaler). 日本語での使い方は [シーダンス](https://emaki.ai/) へ。

MIT licensed.
