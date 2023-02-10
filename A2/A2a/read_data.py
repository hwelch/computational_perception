import h5py

filename = "C:\Users\hunte\Documents\GitHub\computational_perception\A2\A2a\data.h5"


with h5py.File(filename, "r") as f:
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]
    print(type(f[a_group_key])) 
    data = list(f[a_group_key])
    