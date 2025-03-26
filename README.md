[English](./README.md) | [简体中文](./README-CN.md)

# MlxPersistentNaming

Persistent naming for Mellanox network card device identifier

## Highlights

Standardizing the identification of Mellanox Ethernet cards can significantly improve operational efficiency, avoid issues caused by dynamic naming, simplify automation, and facilitate cluster expansion and troubleshooting. This naming convention is particularly well-suited for large-scale compute clusters or high-performance networking environments, ensuring the stability and consistency of network configurations.

## Create udev rules

```python
python3 rename.py
```
create 70-persistent-net.rules file in the /etc/udev/rules.d/ with the content being the result of executing above script.

## Reboot the machine to apply the configuration

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
## Precautions

The modified Mellanox network card identifier name must not be the same as the previous one; otherwise, it will not take effect.




