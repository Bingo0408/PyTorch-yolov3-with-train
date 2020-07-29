def parse_model_config(path):
    """ 读取yolov3.cfg, 生成配置项 """
    file = open(path, 'r')
    lines = file.read().split('\n')
    lines = [x for x in lines if x and not x.startswith('#')]
    lines = [x.rstrip().lstrip() for x in lines]
    blocks = []
    for line in lines:
        if line.startswith('['):
            blocks.append({})
            blocks[-1]['type'] = line[1:-1].rstrip()
            """ 默认的BN层设置为不启用（YOLO之前的卷积层没有BN）"""
            if blocks[-1]['type'] == 'convolutional':
                blocks[-1]['batch_normalize'] = 0
        else:
            """ 按照配置写入, 此时如果有BN配置会自动覆盖 """
            key, value = line.split("=")
            value = value.strip()
            blocks[-1][key.rstrip()] = value.strip()
    return blocks


def parse_data_config(path):
    """ 读取coco.data, 生成配置项 """
    options = dict()
    options['gpus'] = '0,1,2,3'
    options['num_workers'] = '10'
    with open(path, 'r') as fp:
        lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue
        key, value = line.split('=')
        options[key.strip()] = value.strip()
    return options

