### How to use this firmware

Install KMK onto the ItsyBitsy and put this .py into the root directory. Edit and save it as you please. If you want to disable USB drive function in CircuitPy, edit boot.py by adding this code: 
```python
import storage
storage.disable_usb_drive()
```
Save, and then press the reset button or replug the device.

To undo this i.e. to re-enable the drive, plug the board in and double-tap the ItsyBitsy's reset button slowly to enter safe mode. The drive should show up and you can edit boot.py to remove the function; however, it will not run any code even after you've saved boot.py or code.py like normal behaviour. You need to press the reset button or replug the device to jump out of safe mode.
