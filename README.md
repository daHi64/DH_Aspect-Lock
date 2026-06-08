# DH_Aspect Lock (Auto Aspect Lock)

A Blender add-on that automatically maintains the aspect ratio when changing render resolution X or Y in the Output Properties.

---

## Features

* Automatically locks the aspect ratio between resolution X and Y
* Change either X or Y — the other updates to match
* One-click X/Y swap button
* Displays effective pixel resolution (considering Resolution %)
* Toggle on/off from the Output Properties panel
* Works with Blender's native Format resolution UI
* Lightweight, no external dependencies

---

## Compatibility

Blender 3.0 / 4.x / 5.x compatible

---

## Installation

1. Download `DH_Aspect Lock.py`
2. Open Blender
3. Go to `Edit → Preferences → Add-ons`
4. Click `Install`
5. Select `DH_Aspect Lock.py`
6. Enable the add-on

---

## Usage

1. Go to `Output Properties` → `Format`
2. Check `解像度比率を固定` (Lock Aspect Ratio)
3. Change either `Resolution X` or `Resolution Y`
4. The other value updates automatically to maintain the aspect ratio
5. Use the `⇄` button to swap X and Y values instantly
6. The effective pixel resolution is shown below the toggle (updated in real time)

### Note
- The aspect ratio is captured when you enable the lock
- Changing both values manually is still possible when the lock is off

---

## Location

```
Output Properties
 └ Format
    └ 解像度比率を固定 (checkbox)  [⇄]
```

---

## License

This project is licensed under the MIT License.
See LICENSE.

---

## Author

Dahi64

---

## Changelog

See CHANGELOG.md
