from ky038 import KY038

KY038.calibrate()
print("Calibrated")
while True:
    print(KY038.count_claps())
