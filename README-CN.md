# MlxPersistentNaming
永久性修改Mellanox网卡设备标识符
## 亮点
标准化Mellanox以太网卡的识别可以显著提高操作效率，避免动态命名引起的问题，简化自动化流程，并促进集群扩展和故障排除。这种命名约定特别适用于大规模计算集群或高性能网络环境，确保网络配置的稳定性和一致性。

## 创建udev规则
/etc/udev/rules.d/70-persistent-net.rules
### 示例
参数KERNELS对应的是Mellanox网卡的busid

```shell
# udevadm info /sys/class/infiniband/mlx5_0  | grep infiniband/mlx5_0
P:/devices/pci0000:0b/0000:0b:01.0/0000:0c:00.0/0000:0d:00.0/0000:0e:00.0/infiniband/mlx5_0
E:DEVPATH=/devices/pci0000:0b/0000:0b:01.0/0000:0c:00.0/0000:0d:00.0/0000:0e:00.0/infiniband/mlx5_0
```
mlx5_0 busid 是 0000:0e:00.0,以此类推找到其他网卡的KERNELS参数。

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
## 重启机器使配置生效
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
## 注意事项
修改后的Mellanox网卡标识名称不能与之前的名称相同，否则将不会生效。





