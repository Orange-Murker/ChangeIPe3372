## A simple class for changing the IP of a Huawei E3372 by reconnecting it to the mobile network

You may find this useful if your 4G dongle disconnects from the internet periodically

---
### Installation


```
pip install requests
```

Copy the `reconnectE3372.py` file to the folder with your project

---

### Usage

```python
import reconnectE3372
etools = reconnectE3372.IPTools()

# Change IP
etools.changeip()

# Print the new IP
print(etools.ip)
```