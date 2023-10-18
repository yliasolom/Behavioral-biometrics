conf = {
    "WORK_PATH": "./work",
    "CUDA_VISIBLE_DEVICES": "0",
    "data": {
        'dataset_path': "/content/drive/MyDrive/CSTL/data/datasets/sil_128x88", #your_dataset_path
        'resolution': '64',
        'dataset': 'CASIA-B',
        # In CASIA-B, data of subject #5 is incomplete.
        # Thus, we ignore it in training.
        'pid_num': 73,
        'pid_shuffle': False,
    },
    "model": {
        'hidden_dim': 256,
        'lr': 1e-4,
        'hard_or_full_trip': 'full',
        'batch_size': (2, 2),
        'restore_iter': 0,
        'total_iter': 15000,
        'margin': 0.2,
        'num_workers': 4,
        'frame_num': 30,
        'model_name': 'CSTL',
    },
}
