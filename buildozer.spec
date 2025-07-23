[app]
title = Prediksi Saham AI
package.name = prediksisaham
package.domain = org.satria.saham
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,yfinance,ta-lib,scikit-learn,torch,numpy,pandas
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.allow_backup = True