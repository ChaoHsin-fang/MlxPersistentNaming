# MlxPersistentNaming

永久性修改Mellanox网卡设备标识符

## 亮点

标准化Mellanox以太网卡的识别可以显著提高操作效率，避免动态命名引起的问题，简化自动化流程，并促进集群扩展和故障排除。
这种命名约定特别适用于大规模计算集群或高性能网络环境，确保网络配置的稳定性和一致性。

## 创建udev规则

```python
python3 rename.py
```
在/etc/udev/rules.d/目录下新建文件70-persistent-net.rules，内容为上面脚本执行结果

## 重启机器使配置生效

```shell
ibdev2netdev 

mlx5_100 port 1 ==> ibs100np0 (Up)
mlx5_101 port 1 ==> ibs101np0 (Up)
mlx5_102 port 1 ==> ibs102np0 (Up)
mlx5_103 port 1 ==> ibs103np0 (Up)
mlx5_104 port 1 ==> ibs104np0 (Up)
mlx5_105 port 1 ==> ibs105np0 (Up)
mlx5_106 port 1 ==> ibs106np0 (Up)
mlx5_107 port 1 ==> ibs107np0 (Up)
```
## 注意事项
修改后的Mellanox网卡标识名称不能与之前的名称相同，否则将不会生效。





