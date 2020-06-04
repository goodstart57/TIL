# AWS EC2 EBS(하드디스크) 크기 변경하기

## 1. ESB 볼륨 확장

1) AWS console의 인스턴스에 접속하여 원하는 인스턴스 선택

2) 설명 > 루트 디바이스 > EBS ID 클릭

```
/dev/sda1
```

3) 작업 > 볼륨 수정에서 원하는 설정으로 변경


## 2. 파티션 크기 조절하기

1) lsblk로 파티션별 크기 체크

```cmd
$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0         7:0    0   18M  1 loop /snap/amazon-ssm-agent/1455
loop1         7:1    0   18M  1 loop /snap/amazon-ssm-agent/1566
loop2         7:2    0 93.9M  1 loop /snap/core/9066
loop3         7:3    0   97M  1 loop /snap/core/9289
nvme0n1     259:0    0    20G  0 disk 
└─nvme0n1p1 259:1    0    8G  0 part /
```

예시에 따르면 nvme0n1p1 파티션에 8G가 할당되어있으며

아직 할당되지 않은 볼륨 12G를 nvme0n1p1에 할당해야 한다.

```cmd
$ df -Th
Filesystem     Type      Size  Used Avail Use% Mounted on
udev           devtmpfs  970M     0  970M   0% /dev
tmpfs          tmpfs     197M  776K  196M   1% /run
/dev/nvme0n1p1 ext4      7.7G  5.7G  2.1G  73% /
tmpfs          tmpfs     981M  8.0K  981M   1% /dev/shm
tmpfs          tmpfs     5.0M     0  5.0M   0% /run/lock
tmpfs          tmpfs     981M     0  981M   0% /sys/fs/cgroup
/dev/loop0     squashfs   18M   18M     0 100% /snap/amazon-ssm-agent/1455
/dev/loop1     squashfs   18M   18M     0 100% /snap/amazon-ssm-agent/1566
/dev/loop2     squashfs   94M   94M     0 100% /snap/core/9066
tmpfs          tmpfs     197M   12K  197M   1% /run/user/1001
/dev/loop3     squashfs   98M   98M     0 100% /snap/core/9289
```

할당할 파티션의 파일시스템 종류는 `df -Th`을 이용하여 `ext4 파일시스템`으로 확인 가능하다

> 파일시스템의 종류에 따라 명령어가 다르다


2) 파티션 크기 조정 (growpart)

```console
$ sudo growpart /dev/xvdf 1
```

디바이스 이름과 파티션번호를 인자로 추가


3) 파티션 크기 다시 체크

```cmd
$ lsblk
```


4) 파일시스템 확장
```cmd
$ sudo resize2fs /dev/xvdf1
```

5) 디스크 용량 확인
```cmd
$ df -h
```