# MlxPersistentNaming
Persistent Naming for Mellanox Ethernet interfaces
## Highlights
Standardizing the identification of Mellanox Ethernet cards can significantly improve operational efficiency, avoid issues caused by dynamic naming, simplify automation, and facilitate cluster expansion and troubleshooting. This naming convention is particularly well-suited for large-scale compute clusters or high-performance networking environments, ensuring the stability and consistency of network configurations.

## Create udev rules
/etc/udev/rules.d/70-persistent-net.rules
### Example

KERNELS parameter corresponds to the busid of the Mellanox network card

```shell
# udevadm info /sys/class/infiniband/mlx5_0  | grep infiniband/mlx5_0
P:/devices/pci0000:0b/0000:0b:01.0/0000:0c:00.0/0000:0d:00.0/0000:0e:00.0/infiniband/mlx5_0
E:DEVPATH=/devices/pci0000:0b/0000:0b:01.0/0000:0c:00.0/0000:0d:00.0/0000:0e:00.0/infiniband/mlx5_0
```
mlx5_0 busid is 0000:0e:00.0,similarly,find the busid of other network cards and fill it in the KERNELS parameter.

```shell
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", KERNELS=="0000:f1:00.0", NAME="ens100np0"
SUBSYSTEM=="infiniband", ACTION=="add", KERNELS=="0000:f1:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_100"

SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", KERNELS=="0000:22:00.0", NAME="ens101np0"
SUBSYSTEM=="infiniband", ACTION=="add", KERNELS=="0000:22:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_101"

SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", KERNELS=="0000:47:00.0", NAME="ens102np0"
SUBSYSTEM=="infiniband", ACTION=="add", KERNELS=="0000:47:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_102"

SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", KERNELS=="0000:5b:00.0", NAME="ens103np0"
SUBSYSTEM=="infiniband", ACTION=="add", KERNELS=="0000:5b:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_103"

SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", KERNELS=="0000:97:00.0", NAME="ens104np0"
SUBSYSTEM=="infiniband", ACTION=="add", KERNELS=="0000:97:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_104"

SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", KERNELS=="0000:dd:00.0", NAME="ens105np0"
SUBSYSTEM=="infiniband", ACTION=="add", KERNELS=="0000:dd:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_105"

SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", KERNELS=="0000:c3:00.0", NAME="ens106np0"
SUBSYSTEM=="infiniband", ACTION=="add", KERNELS=="0000:c3:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_106"

SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", KERNELS=="0000:s2:00.0", NAME="ens107np0"
SUBSYSTEM=="infiniband", ACTION=="add", KERNELS=="0000:s2:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_107"

```
## Reboot the machine to apply the configuration
```shell
ibdev2netdev 
mlx5_100 port 1 ==> ens100np0 (Up)
mlx5_101 port 1 ==> ens101np0 (Up)
mlx5_102 port 1 ==> ens102np0 (Up)
mlx5_103 port 1 ==> ens103np0 (Up)
mlx5_104 port 1 ==> ens104np0 (Up)
mlx5_105 port 1 ==> ens105np0 (Up)
mlx5_106 port 1 ==> ens106np0 (Up)
mlx5_107 port 1 ==> ens107np0 (Up)
```
## Precautions
The modified Mellanox network card identifier name must not be the same as the previous one; otherwise, it will not take effect.




