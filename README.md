# OpenOOD: Benchmarking Generalized OOD Detection
[![paper](https://img.shields.io/badge/Paper-In%20Process-b31b1b?style=for-the-badge)]()
&nbsp;&nbsp;&nbsp;
[![paper](https://img.shields.io/badge/Integrate-30+%20Methods-228c22?style=for-the-badge)]()
&nbsp;&nbsp;&nbsp;
[![paper](https://img.shields.io/badge/Support-Dist%20Training-797ef6?style=for-the-badge)]()


<img src="https://live.staticflickr.com/65535/52145428300_78fd595193_k.jpg" width="800">


This repository reproduces representative methods within the [`Generalized Out-of-Distribution Detection Framework`](https://arxiv.org/abs/2110.11334),
aiming to make a fair comparison across methods that initially developed for anomaly detection, novelty detection, open set recognition, and out-of-distribution detection.
This codebase is still under construction.
Comments, issues, contributions, and collaborations are all welcomed!

| ![timeline.jpg](https://live.staticflickr.com/65535/52144751937_95282e7de3_k.jpg) |
|:--:|
| <b>Timeline of the methods that OpenOOD supports.</b>|


## Updates
- **14 June, 2022**: We release `v0.5`.
- **12 April, 2022**: Primary release to support [Full-Spectrum OOD Detection](https://arxiv.org/abs/2204.05306).

## Get Started


To setup the environment, we use `conda` to manage our dependencies.

Our developers use `CUDA 10.1` to do experiments.

You can specify the appropriate `cudatoolkit` version to install on your machine in the `environment.yml` file, and then run the following to create the `conda` environment:
```bash
conda env create -f environment.yml
conda activate openood
```

Datasets and pretrained models are provided [here](https://entuedu-my.sharepoint.com/:f:/g/personal/jingkang001_e_ntu_edu_sg/Eso7IDKUKQ9AoY7hm9IU2gIBMWNnWGCYPwClpH0TASRLmg?e=kMrkVQ).
Please unzip the files if necessary.

Our codebase accesses the datasets from `./data/` and pretrained models from `./results/checkpoints/` by default.
```
├── ...
├── data
│   ├── benchmark_imglist
│   ├── images_classic
│   ├── images_medical
│   └── images_largescale
├── openood
├── results
│   ├── checkpoints
│   └── ...
├── scripts
├── main.py
├── ...
```

The easiest hands-on script is to train LeNet-5 on MNIST and evaluate its OOD or FS-OOD performance with MSP baseline.
```bash
sh scripts/basics/mnist/train_mnist.sh
sh scripts/ood/msp/mnist_test_ood_msp.sh
```

---
## Supported Benchmarks (10)
This part lists all the benchmarks we support. Feel free to include more.

<img src="https://live.staticflickr.com/65535/52146310895_7458dd8cbc_k.jpg" width="800">

<details open>
<summary><b>Anomaly Detection (1)</b></summary>

> - [x] [MVTec-AD](https://www.mvtec.com/company/research/datasets/mvtec-ad)
</details>

<details open>
<summary><b>Open Set Recognition (4)</b></summary>

> - [x] [MNIST-4/6]()
> - [x] [CIFAR-4/6]()
> - [x] [CIFAR-40/60]()
> - [x] [TinyImageNet-20/180]()
</details>

<details open>
<summary><b>Out-of-Distribution Detection (5)</b></summary>

> - [x] [BIMCV (A COVID X-Ray Dataset)]()
>      > Near-OOD: `CT-SCAN`, `X-Ray-Bone`;<br>
>      > Far-OOD: `MNIST`, `CIFAR-10`, `Texture`, `Tiny-ImageNet`;<br>
>      > Robust-ID: `ActMed`;
> - [x] [MNIST]()
>      > Near-OOD: `NotMNIST`, `FashionMNIST`;<br>
>      > Far-OOD: `Texture`, `CIFAR-10`, `TinyImageNet`, `Places365`;<br>
>      > Robust-ID: `SVHN`;
> - [x] [CIFAR-10]()
>      > Near-OOD: `CIFAR-100`, `TinyImageNet`;<br>
>      > Far-OOD: `MNIST`, `SVHN`, `Texture`, `Places365`;<br>
>      > Robust-ID: `CINIC-10`;
> - [x] [CIFAR-100]()
>      > Near-OOD: `CIFAR-10`, `TinyImageNet`;<br>
>      > Far-OOD: `MNIST`, `SVHN`, `Texture`, `Places365`;<br>
>      > Robust-ID: `CIFAR-100-C`;
> - [x] [ImageNet-1K]()
>      > Near-OOD: `Species`, `iNaturalist`, `ImageNet-O`, `OpenImage-O`;<br>
>      > Far-OOD:  `Texture`, `MNIST`;<br>
>      > Robust-ID: `ImageNet-v2`;
</details>



---
## Supported Backbones (6)
This part lists all the backbones we will support in our codebase, including CNN-based and Transformer-based models. Backbones like ResNet-50 and Transformer have ImageNet-1K/22K pretrained models.

<details open>
<summary><b>CNN-based Backbones (4)</b></summary>

> - [x] [LeNet-5](http://yann.lecun.com/exdb/lenet/)
> - [x] [ResNet-18](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html)
> - [x] [WideResNet-28](https://arxiv.org/abs/1605.07146)
> - [x] [ResNet-50](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html) ([BiT](https://github.com/google-research/big_transfer))
</details>


<details open>
<summary><b>Transformer-based Architectures (2)</b></summary>

> - [x] [ViT](https://github.com/google-research/vision_transformer) ([DeiT](https://github.com/facebookresearch/deit))
> - [x] [Swin Transformer](https://openaccess.thecvf.com/content/ICCV2021/html/Liu_Swin_Transformer_Hierarchical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper.html)
</details>

---
## Supported Methods (34)
This part lists all the methods we include in this codebase. In `v0.5`, we totally support **more than 32 popular methods** for generalized OOD detection.

All the supported methodolgies can be placed in the following four categories.

![density] &nbsp; ![reconstruction] &nbsp; ![classification] &nbsp; ![distance]

We also note our supported methodolgies with the following tags if they have special designs in the corresponding steps, compared to the standard classifier training process.

![preprocess] &nbsp; ![extradata] &nbsp; ![training] &nbsp; ![postprocess]

<!--
density: d0e9ff,
reconstruction: c2e2de,
classification: fdd7e6,
distance: f4d5b3 -->

<details open>
<summary><b>Anomaly Detection (5)</b></summary>

> - [x] [![](https://img.shields.io/badge/ICML'18-Deep&#8211;SVDD-f4d5b3?style=for-the-badge)](https://github.com/lukasruff/Deep-SVDD-PyTorch) ![training] ![postprocess]
> - [x] [![](https://img.shields.io/badge/arXiv'20-KDAD-f4d5b3?style=for-the-badge)]()
![training] ![postprocess]
> - [x] [![](https://img.shields.io/badge/CVPR'21-CutPaste-d0e9ff?style=for-the-badge)](https://github.com/lukasruff/Deep-SVDD-PyTorch)
![training] ![postprocess]
> - [x] [![](https://img.shields.io/badge/arXiv'21-PatchCore-f4d5b3?style=for-the-badge)](https://github.com/lukasruff/Deep-SVDD-PyTorch) ![training] ![postprocess]
> - [x] [![](https://img.shields.io/badge/ICCV'21-DRÆM-c2e2de?style=for-the-badge)](https://github.com/lukasruff/Deep-SVDD-PyTorch) ![training] ![postprocess]
</details>


<details open>
<summary><b>Open Set Recognition (3)</b></summary>

> No Extra Data (2):
> - [x] [![](https://img.shields.io/badge/CVPR'16-OpenMax-d0e9ff?style=for-the-badge)](https://github.com/13952522076/Open-Set-Recognition) ![training] ![postprocess]
> - [x] [![](https://img.shields.io/badge/TPAMI'21-ARPL-f4d5b3?style=for-the-badge)](https://github.com/iCGY96/ARPL) ![training] ![postprocess]

> With Extra Data (1):
> - [x] [![](https://img.shields.io/badge/ICCV'21-OpenGAN-fdd7e6?style=for-the-badge)](https://github.com/aimerykong/OpenGAN/tree/main/utils) ![training] ![postprocess]
</details>


<details open>
<summary><b>Out-of-Distribution Detection (20)</b></summary>

<!--
density: d0e9ff,
reconstruction: c2e2de,
classification: fdd7e6,
distance: f4d5b3 -->

> No Extra Data (17):
> - [x] [![msp](https://img.shields.io/badge/ICLR'17-MSP-fdd7e6?style=for-the-badge)]()
> - [x] [![odin](https://img.shields.io/badge/ICLR'18-ODIN-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![postprocess]
> - [x] [![mds](https://img.shields.io/badge/NeurIPS'18-MDS-f4d5b3?style=for-the-badge)]() &nbsp;&nbsp; ![postprocess]
> - [x] [![confbranch](https://img.shields.io/badge/arXiv'18-ConfBranch-fdd7e6?style=for-the-badge)](https://github.com/uoguelph-mlrg/confidence_estimation) &nbsp;&nbsp; ![preprocess] &nbsp; ![training]
> - [x] [![godin](https://img.shields.io/badge/CVPR'20-G&#8211;ODIN-fdd7e6?style=for-the-badge)](https://github.com/guyera/Generalized-ODIN-Implementation)  &nbsp;&nbsp; ![training] &nbsp; ![postprocess]
> - [x] [![gram](https://img.shields.io/badge/ICML'20-Gram-f4d5b3?style=for-the-badge)](https://github.com/VectorInstitute/gram-ood-detection)  &nbsp;&nbsp; ![postprocess]
> - [x] [![duq](https://img.shields.io/badge/ICML'20-DUQ-f4d5b3?style=for-the-badge)](https://github.com/y0ast/deterministic-uncertainty-quantification)  &nbsp;&nbsp; ![postprocess]
> - [x] [![csi](https://img.shields.io/badge/NeurIPS'20-CSI-fdd7e6?style=for-the-badge)](https://github.com/alinlab/CSI)  &nbsp;&nbsp; ![preprocess] &nbsp; ![training] &nbsp; ![postprocess]
> - [x] [![ebo](https://img.shields.io/badge/NeurIPS'20-EBO-d0e9ff?style=for-the-badge)](https://github.com/wetliu/energy_ood) &nbsp;&nbsp; ![postprocess]
> - [x] [![mos](https://img.shields.io/badge/CVPR'21-MOS-fdd7e6?style=for-the-badge)](https://github.com/deeplearning-wisc/large_scale_ood)  &nbsp;&nbsp; ![training]
> - [x] [![gradnorm](https://img.shields.io/badge/NeurIPS'21-GradNorm-fdd7e6?style=for-the-badge)](https://github.com/deeplearning-wisc/gradnorm_ood) &nbsp;&nbsp; ![postprocess]
> - [x] [![react](https://img.shields.io/badge/NeurIPS'21-ReAct-fdd7e6?style=for-the-badge)](https://github.com/deeplearning-wisc/react) &nbsp;&nbsp; ![postprocess]
> - [x] [![vos](https://img.shields.io/badge/ICLR'22-VOS-d0e9ff?style=for-the-badge)](https://github.com/deeplearning-wisc/vos) &nbsp;&nbsp; ![training] &nbsp; ![postprocess]
> - [x] [![vim](https://img.shields.io/badge/CVPR'22-VIM-fdd7e6?style=for-the-badge)](https://ooddetection.github.io/) &nbsp;&nbsp; ![postprocess]
> - [x] [![sem](https://img.shields.io/badge/arXiv'22-SEM-d0e9ff?style=for-the-badge)](https://arxiv.org/abs/2204.05306) &nbsp;&nbsp; ![preprocess] &nbsp; ![training] &nbsp; ![postprocess]
> - [x] [![mls](https://img.shields.io/badge/ICML'22-MLS-fdd7e6?style=for-the-badge)](https://github.com/hendrycks/anomaly-seg) &nbsp;&nbsp; ![postprocess]
> - [x] [![kld](https://img.shields.io/badge/ICML'22-KL&#8211;Matching-fdd7e6?style=for-the-badge)](https://github.com/hendrycks/anomaly-seg) &nbsp;&nbsp; ![postprocess]
> - [x] [![kld](https://img.shields.io/badge/ICML'22-LogitNorm-fdd7e6?style=for-the-badge)](https://github.com/hongxin001/logitnorm_ood) &nbsp;&nbsp; ![training] &nbsp; ![preprocess]


> With Extra Data (3):
> - [x] [![oe](https://img.shields.io/badge/ICLR'19-OE-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![extradata]
> - [x] [![mcd](https://img.shields.io/badge/ICCV'19-MCD-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![extradata] &nbsp; ![training]
> - [x] [![udg](https://img.shields.io/badge/ICCV'21-UDG-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![extradata] &nbsp; ![training]
</details>


<details open>
<summary><b>Other Methods on Robustness and Uncertainty (6)</b></summary>

> - [x] [![mcdropout](https://img.shields.io/badge/ICML'16-MC&#8211;Dropout-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![training] &nbsp; ![postprocess]
> - [x] [![deepensemble](https://img.shields.io/badge/NeurIPS'17-Deep&#8211;Ensemble-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![training]
> - [x] [![tempscale](https://img.shields.io/badge/ICML'17-Temp&#8211;Scaling-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![postprocess]
> - [x] [![mixup](https://img.shields.io/badge/ICLR'18-Mixup-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![preprocess]
> - [x] [![cutmix](https://img.shields.io/badge/ICCV'19-CutMix-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![preprocess]
> - [x] [![pixmix](https://img.shields.io/badge/CVPR'21-PixMix-fdd7e6?style=for-the-badge)]() &nbsp;&nbsp; ![preprocess]
</details>


---
## Contributing
We appreciate all contributions to improve OpenOOD.
We sincerely welcome community users to participate in these projects. Please refer to [CONTRIBUTING.md](https://github.com/Jingkang50/OpenOOD/blob/v0.5/CONTRIBUTING.md) for the contributing guideline.

## Contributors
<a href="https://github.com/jingkang50/openood/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jingkang50/openood" />
</a>


## Citation
If you find our repository useful for your research, please consider citing our paper:
```bibtex
@article{yang2022openood,
    author = {Yang, Jingkang and {\textit{et al.}}},
    title = {OpenOOD: Benchmarking Generalized Out-of-Distribution Detection},
    year = {2022}
}

@article{yang2022fsood,
    title = {Full-Spectrum Out-of-Distribution Detection},
    author = {Yang, Jingkang and Zhou, Kaiyang and Liu, Ziwei},
    journal={arXiv preprint arXiv:2204.05306},
    year = {2022}
}

@article{yang2021oodsurvey,
    title={Generalized Out-of-Distribution Detection: A Survey},
    author={Yang, Jingkang and Zhou, Kaiyang and Li, Yixuan and Liu, Ziwei},
    journal={arXiv preprint arXiv:2110.11334},
    year={2021}
}

```







[density]: https://img.shields.io/badge/Density-d0e9ff?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAACuElEQVRoge2Zu2tUQRSHv9UomO0SFKNBrJQkFnY2Ij6iJig+EMRKbIUk+B9YWxn/gdSCIIIkgmiChY3BwkZN8IVoIgQECw0KSSxmxj1z9e7eOTObXeR+cGEm95wz58e8zt1AScm68AR4a58DLc4liI5Mfxew27a3rHMuUWxodQKpKIW0G6WQdqMU0m5k75GUdAJHgb3AGjAHTAPLTRzzD+/toGvAYWWMCjAGLIlY7lkCRq1NU4kVUgEm+FtA9pmgyWJihdzCT/gbMAU8sG357maCfHOJETKEn+hjoEe877F/kzYnIvPNRSukM+P7DKj+w64KzAq7dzSpONUKGRV+P4GBOrb7rI2zv6rKtAEaIZuAD8JvvIDPOP6sJL8GNEIuCJ9fmG+aRvTiz8rZ4EwzpLjZL4v2HeBjAZ9PwF3Rv5IgD4/QGenGzILzOR4w1kn8fdUVlGmG2BkZxuwRgAXM8VqUR8AX296MOb7VxAo5Jdr3gdUA3xVgMidWMDFCNuIvpck8wzpInyESnl4he+SQsP2BuRRDqWKqYRfnoCIGEDcjw6I9gxETynfMb2kO9fKKESLrpKmIOHJ5Jau9ii6tbsxmdbZ7IsbsE3FWgK2aINoZGRS+n4F5ZRyAV5gL0uVzRBMkRojjoTKGZFq0j2kCpBAScgnmIWMM5loFUGSPDAibVfyPJy07bCwXtz80gGZGzov2LLCoiJFlAXgu+udCA2iEyJL7nsI/DxkruqxvtLR24i+BvtgBBf34S7Y3xDl0Ri5R+xlnHnN0puIltWO8AlwMcQ4R0gGMiP7tkIEKImOOYApTFfWW1jXxbhnYrh2kDtswNZsbZ6yoY72y+TS10qMLuC7evQbOhOVYmDlgv23fwFTVX21/EfPd0xA5I+34zOQl/t/+W+Ep8KYViRTkRasTKCkpKUnDb6XM8jMAxEX4AAAAAElFTkSuQmCC

[reconstruction]: https://img.shields.io/badge/Reconstruction-c2e2de?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAADj0lEQVRoge3aS2tdVRQH8F80bS5Y2yYx1qEFrYpSMxBHKjrRFEV8oFB1Wuqotv0A+h3EfBQpitLGRGhsrQ9Ek0adVIUKWvARoxWvg7U35yTcpLnnnnvuLfQPhwX7+V/7sfbaax9uYLgw0kAf83gYf+IyvsfXWMBHuNIAh1owj/Ym3794D69hbFAEu8EOjOM+PIc3cRprCqV+xEm06uhwq9Hb+NWBvTiC86V2v8WhXhtuWpEyZvBZqf1ZNc1OGVM4q7+KwM14A6upj3PYV1fjd2IlNfyd/iqScRDLqZ8V7O+1wduwlBr8RIxOE4oQxmFBMYB3VG2oJaY2T/GtKb0pReAWxZI+p+KeeUcxtVOl9CYVgUnFMpvttvLT+E/Y+ekNeU0rQuyZbABmtltpp2Jzn+iQPwhF4LhihWxriZ1IFb7CaIf8QSkyis9T38evVXgHfkqFNztd54WzNwgcEtx+cA3f7HAq+EUDpKpgBJ8Kjq9sVfCDVOhIA6Sq4qjgeGqzArvxD66Kw2hYMY6/Bc89nQq8KDQ90yCpqjgjuD6bE24qZT6U5OkmGVVEHuxHckJZkYNJftkYnerIxujenFBW5O4kv2mMTnVcTPJATigrsjfJXxqjUx2Xk5zolJnvz9dDEGBMcF3LCeUZyaGhQbgfPaOsyB9J7hoEkS6xO8nfckJZkbw3arsj9xG3J/lrTigrspLkAcOPe5LM1mudItnsPtgYnerIZ95STigrspDk443RqY4nkux4nRgXsdg1xZkyjJhQOI1506+bkSv4UNjolxql1h1eFtfx95Ws1ka8Ks6R8w2R6hYjuCA4Ht6q4Ji4RrbxVP95dY1nBLdLtuGBnEyFL4hY7LBgVHi9bRzbToWWCO23RUB5WJAHeFkX/mCOVqwqbPYgMY2/BKcnu608qxiByXp5dYUpRcDw7SoNlIPYZ0VAuWnswmLisKiHK8aU9c8KU1sXrxUT+FjxHNezM7tfMbXLmvHFpkt9XhSPTbVgn2KZrYrYa6e4cK8YFdYpb+xFhcteG1oKA9AWAeWeX18TRsRTRj4n8sbu67V7RjHtbRGLPapadHICryvcjryUujaxVdESyyu7M23hkc7hLTyP+4XZ3pm+STyAF1KZuVQn178kTuyBBD/GRFT8lLgCbPeNPn9X8a5wAHtSoM6favbgMTwqftW4S5jr/Ij6O34WpnRJvLPM2cIVv4HrGf8Dfs0JOaMPQmgAAAAASUVORK5CYII=

[classification]: https://img.shields.io/badge/Classification-fdd7e6?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD3klEQVRogcWZu09UQRTGfwILhTw0cQFRG0tQEwsrG4ydiQExFsQEY6h4KJLYU6M22qGxImpjYvwHLBQBDSq6KqBg1MSOGOWlaHAtztnMZbl79965j/2SCRvuzPnm3Jlz5ptzwaAKuABMAivaJoB+oJLoECvPHmAayBZoL4GmsCRx81Q5jL8D2oAabe3AjD57Qbg3FjvPRTXwHqhzeV7nIOmzIUiK55kObvPoc0r7TNgQJMWzrINrPPrUap8lG4IkeMp0YDFsc/S3xZ8APIFRhuxZgOMe/XLPMrZEyP73y/PWhqAfWZUZ3INwBzCnfbpsCBTdAXh6bQgqkfydBWaRgKvV1uEwvg402hAoUsCYD54p7WuFJowzbm1d/2aAelsSoAF44sEzBewOYR+QlekDxpEMs4qkwS5kJTJE48w+tbOhHMvAU2Q7Wa9EEKSBN5h9bvvmLquNBxHNywppzMrMYufMax3fHuG8rFDPZmeCiLzDOm4R0V4lRwMi/HLayZnNUkAncBdYQOJgDZhHzocscCPJyRZDA+KE05l24AuFs1KuLQAnk59yYTRinFnETDSDqN1mYLu2FmAAkzD+AcOEkCVRoxHjxG8kjXppsjKgR/tmgStxT9Av2jFOtAYY14pxxkvaJ4IUJiZ6LMb36thPRFsXCIxOTEzYSPxyTCo/E2YiYe4XYDLPLSR4g2IDuK2/T4ecSygsIG+zOYSNFkxKdkMKuQKMIUklljLVik6iOoSNGrWx6vIsjSjiuMtUrFH8Hl4MOUd+5f2/AnhF/GUqIJqtdQBzQE4DI8B5YIhkylQA3FNDAyFsDOItZ+IuUwGSabKI7LBNvzkheQ44ClwC7mAcibtMBcjenMf+QMwVPj6z9Xa4RHFH6ojIkQrgPnYS5RimFuCmhCcpfgHr0D7jAXi3IA08wgSqUzSWe4wrR1Yi58RwgX5BylRW5SOAI8BXNfIN2dtDGIcyyF5vQc6YaiQ7DWJiIgtcpbCM91umsi4fdWNU62M23w5PKGmxi5Xf4kOxMpVr+cjtS9IkssRV2kYcRq7j/iZSyNsbRc6AZbX1Abn+9gF/ka2134cz+WUqz/KRny9JueBbBc76mIAXbqqt0ZB2NsHvl6QskmoPRcC5F5EkG8DBCOwBwb4kWWcHF1xTmw+jMhjkS9JYVKTALuAnJmhXCSnRg3xJ+h7UuAfSSAKITKInKgUUFcBztfkRORdqCSnRE5MCDvSovTnkhM6HlURPRArkYVztdXj0CSzRY5cCLvihNnd69LGS6FZSIARijctAUiAkShGXsaAUcRkLShGXsSHpuIwVkcXlf7gl3GNHJu+DAAAAAElFTkSuQmCC

[distance]: https://img.shields.io/badge/Distance-f4d5b3?style=for-the-badge&&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB3ElEQVRoge2aO07DQBRFDzT5LABFNLRIFIiSgoYC0SGxAgoaPoVXQ4OggR2AxH8XSBErgB4huoTCfnjk2HHi+fiNlNMkhT2ak+vnGzmBBc7ZAo6ApbY3YsMO8A2MgUtgud3tNGMX+CGVGGWvF0SWjJnENbAP/BJZMkUJ2fQeEcmYl9MNk5s1k1F7mZlJjIEPYLXkONXJmEncAsPs/RAYlByvMhlT4or0Ex6Qy5xXnKdKZtpMDICzmvNVyMw6E3W0OjPzzkQdrSRT1hMrwDsRJVM3E7bJHJBfqodWO52CKVG1WRuZLvCQnfsJrFnut5R5ZmKWW2+RLvBILrFuv+VJmvTELLdeIbhEk56oI4iEq56oogPcZWt/ARsO1/7HdU8UCZ6Ey54QOsA9AZPw0RNd4AkFM2GTTPAkfPREjwBJ+O6J4BI+eqIHPKNgJmxQNxNNCJ6Ej57oAS9E3hNqZsImmeBJ+OoJkYi6J7xLbDIpIbjqCe8SkD6ZkJk4drx2MAkhIf2hZQScOFozyGCX4VKmNQnBlDltuEbrEoKNjBoJoYlMH2USwjwyfeAVhRKCKVPVJ+olhGky0UgIZTLRSQgJ+T8UEuCNgI3tGklGvtJElUQRkYlaQtjG7UOIBQB/hf9HJ+Iv7O8AAAAASUVORK5CYII=




[preprocess]: https://img.shields.io/badge/PreProcess-f4d5b3?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAABDUlEQVQ4jc3TPy8EURQF8N8uS/wJGxuh0tH7CBKthk/gk6iIQiFRSEhEFEQhGoSQbERUEo2SGp1CwTa7infJZE3sbuckr5j75p5z7pk7/BesoIZGm6eG5SxBDSMdCFbwmS002mi6xU1zT7ED1fpfQtmLAexhtAVhI++hGyd4wD3KUS/jUJr9G8P8HmETBUzjGqdSuMeYwno4PMMjZrMOlnCHwagVsI23UC9iHNWoz+AlS/CEsSZHXTjABvpwiZ0YdSsc/hBMykcJEziXwi0FSTXGQVqkSl43ekNpHz1BcoV+YQXW8BwvZLGKVymPRexKoc7hQ1y0whHepXzqWJBZ41abWJA+3xAuMK/pH/gCPJhBnIabIDQAAAAASUVORK5CYII=

[training]: https://img.shields.io/badge/Training-f4d5b3?style=social&logo=data:image/png;base64,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


[extradata]: https://img.shields.io/badge/ExtraData-f4d5b3?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAABmJLR0QA/wD/AP+gvaeTAAAGYElEQVR4nO2d228VRRzHP6fl2ipFvECN1gpoQR6MVEXFN28hkQdS0FdFRf0P8E8QjXh5ML6aiAFvKD6p9U2lGkuJxEtiI1ClRWy5lYrc6sNvT/acPbN7dk9nd6dnf59ksifl7G9+85uzM7PznWFKuEcL0A3cCtwE3OJdrweu8dISoN37/kJggff5PPCv9/kcMAGc9K7/AH8CR4AR4A/gMDCdamkSUso5/4XAWuBe77raS20Z5T8F/AL8DBwAvgcG8Ss1c7KukPnAeuAR4GHgTmBuxj7U4yIwBPQDXwDfABdy9cgy7cCTwIfAJNJEzKY06fn+BBk8uWk+IeuBF4FNJC/IaeA3/Pb+CDAGjCP9wQRwxvtuZb9R2Z904Pc31wLLkP7oZu+6CliU0K8p4GPgbeDbhPfmwhzgKeAg8X+Bx4BPgO3AY0BXhv52eXlu93w4lsDvg0hZ52Tob2xagWeAYeoXZBzY7X2/Ow9n69ANPAvsQXytV55hYCsSAyfoBQaoXwnvAhtxrxOPogV4EHgDGCW6jEPAA/m4KSwA3gKuYHbwCvAV0Iejj3VC5gKbkdFXWJkvA28io8lMuQ0Zr5ucugS8B6zJ2qkMWYOU8RLmGAwCK7Nyphc4EeLIZ8DtWTniAD3APsyx+Bt52U2V+4BThsxHgMfTztxhNiIxCMblFBKzVLgR+MuQ6afIOL/odCAjs2B8xpB3H6u0IvM8wcxeI//5MJcoATupjdMAlofFLxgyedlmBk3GDmrj9bwt421IBxVsplpsZdCEtCADnMqYHUemdmbMloDhM0CnDcNNzlJkTq4ydn02DO8OGN1hw2hBeIXq2L1vw+ihgNF7bBgtCOuojt1PNowGH7urbRgtCIuobe4jidMxBzUDHebGJxjfuj/mRkZKPQ3cU1QSx6qRCtnSwD1FZXMaRoMvOGeRaRQlmmXU9r/TNgybZjL3oS+GUbQQPgs8Y8IUMn0fCcc0dZJ6hUwjiqE+KT4l4FWiYzZjooxPI4vJltrIaJZzHeHNVKoVYuqoRhCRpqiECVSZdOprEdElrLNfZSPTWcJq4HPMsRgF7jL8fcaYDK4gfJHDZWAXzb/IYRdSVlMMfgSWe9/NpEJAlrq8TvQyoH7kRXI2rcUKYx6yvvdrosu8k+plQJlVSJm7gf0hDpbTBLNzoVwr/kK540SXcRDzQrnMK6Ts+FbiLSWdAD4AnsN/rF1iObANWfF+kvrlGQaeJnz4n0uFlCkvth4y3BeWRoG9wEvABmRtbRYzyiUvrw1e3nsJH6yY0hDxFlsnqpA4BQ8aiRus+5HFEX3428/iMom/HeGodx3F36I2jqx5AtlMc8773I609eBvRVjife5EKqC8HaEHuKoBvz4C3gG+i3lPo/GLNDiTR64NmfXcg0xMxv0FupLOIjJ2H40tUnDmCTExD3lyHgUeQsbp8yLvyJ4LSAfdD3yJbMy5OAN7ieKXdYUEWYBUyjrvegfyYpm0KWmUSeBX/E2fA0hl/Gcxj1lVISZKyM6mbu/ahWyLvoHqbdFlOXQ+/pa5KfxgnqV6W/QJZFv0US8dRvqmtEm9D0m6L6/ILCZhH6Kaerqopu4Yqqk7hGrqDqGaumOopu4Iqqk7hGrqDqGauiOopu4Iqqk7gGrqDqCaugOopo5q6lVO1SNoRDV11dRzTaqp54xq6qimHu8fGzFoAdXUYxisTKqpx0c1dcdQTd0xVFN3CNXUHUI1dcdQTd0RVFN3CNXUHUI1dUdQTd0RVFN3ANXUHUA1dQdQTR3V1KucqkfQiGrqqqnnmlRTzxnnNfXTVKuEHcT4L7Nj0uyaegd+0woSy8VRN8Q5zm6E6pe8HuCHxK6ZOY+0xZXtcTNp6sFZi5F6N8SpkENUV8gW7FWIiWkkUFksQEiboGJo5XSEzdR2cqoY1sekGG6yYXghtW+pqhhGY1IMrR15BHKgVXD4pophOCbFcJvNDFoxH0C8Ez1PpJISMuEajNN+UjhNuhPzwZKqGAphiuEYMkpMhaijV1UxrI1LqkevlllL7bmGlZ29KoaSMjmcuMxKRBUzOaKKocRmRdZOzUcOcw9zqoiKYW4H3FfSi3kEVpmKoBgewKwY5kKRFcPfEcXQ+rDWBqoYWnAqLVQxdJSiK4aJyHrao4iKYSLynodqdsUwMXlXiIlmUgwVRbHK/zvve/uixi6eAAAAAElFTkSuQmCC



[postprocess]: https://img.shields.io/badge/PostProcess-f4d5b3?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAAFXElEQVR4nO2dW2gdRRjHf7bRIiKiVNSK2IqkCV4ajdfUqEWrSOKt1KpVUi+NN0SliD5oVfClCj4Vi/oo6oNI38UHxUbEB29QwUtVvEWbqmlMTc31+DCNrbDz7ew5szu7O98Pljxk58+3//85s7O7s3NAURRFURRFURRFURRFUVpnAbAGeAP4FpgAGgG3F4HDcj3iEnEh8BlhDY82hJuA/YQ3O8oQVgL/EN7ktO0VTBdZK44AdhHe3GhDuJ/wpkbdHb1H8kH+AQwAxxZYy3JLLbUNoQ2YJvkA+wPUkyWAWoRwMskHtpcwB5Y1gMqfE2wH/GXJ6ildCJVNvEmGgc+F/w8CWynwWxtbAOPAKuBjYZ8HgJcpyJvYAgAYBVYjhzAIvEQB/sQYAJQohFgDgJKEEHMAUIIQYg8AAoegARiChdDmU6wCzF+gNcvggb/3AXOtl6PfgGYYBF7wJaYBNMc1voQ0gMBoAIHRAAJT1wC+wtzRbHXryLvQugZQGTSAwGgAgdEAAqMBBCa2e0FZmR9N5YZ+AwKjAQRGAwiMBhAYDSAwGoAfjgc2Ax8Bu4ExYCdmlt1ZRRRQtrmhRXInxnDbfNNZYBvmBZbciDWAZ3Cf+PsucFRehcQYwNNkn309BBydRzGxBfAozU1/zy2EmAJ4jObNP7Q78npOiCWATcjG7gJWAIuB7Sn7bvNZWAwBPISZjGUz9Adg6SH7LwReF/afBbp8FVf3ADYim/8jsCyhXVoIW30VWOcABkk3/zShfRv27minryLrGsBdmK7CZv7PwOkOOost7cd8FVrHAAaQzR/GHLcLZ1g09vgqtm4BrAdmsJv/G9DpqHUi8IVF50NfBdcpgHXI5o8AZzpqLcF4YNN6ylfRdQlgDTCF3bBRoNtR6xTga0FrHDjBV+F1COB6ZPP/BM5x1DoVs0ybTavBwZc9vFD1APqBSeRP/nmOWsuA7wWtBvCcx9qBagdwFfISa2OYNfBcWAp8J2g1gOc91v4fVQ1gNbL5+4BLHbXagZ8ErQawxWPt/6OKAfRiDLaZ9TdwuaPWcuAXQStX8+cLqFIAKzGjEMn8VY5aHZiLMsn8zR5rT6RKAfQAf2E3awK4wlGrE/hV0GoAT3is3UpVArgI2fxJoM9RqwtzK8GmNQc84rF2kSoEcC5mLC+Zf20Grd8FrTnM84PCKHsAXZjVG22GTQHXOWp1p2jNAQ96rN2JMgewAvnTOgPc7KjVgzwHaA6z4lbhlDWAs5H76RngVketS5DPH7PAHR5rz8QSS1FjhFuPswN5hDID3Oao1Yts/gywwWPtmSnbwq2dmHv2kmG3O2pdibkusGlNA7d4rL1ppKWLNwDHFVRHO/KFUZau4mrkH56YAtZ6rL0l7sVeqI/NhWMwz2mlk+Tdjlp9yEvxTwI3OmoVwuHAN4QNoE9on2WE0od8k24SuMFRq1B6yO8HHFzYYmmbZWzen3IMk7hfMwRhLfn8hIkLQ5a2zzq2X4f8VGwC8/yg9JwPfEKxARyJ/ZPrMoNhPfaRXAMzEnK9SVcKFmD6ydcw54ZWf8Yqjcss7UZIvxYZQJ4JMX5AXxF4kmTztqe0S5v9tg/3ZwNR8zbJBm4S2mxENn8vcHF+JdeHhdhvkl2QsH8HZlKUNOl21NJWSaAbe/exCDM38x7gVcxs5rTzjZqfkYdJNnI/8k20pG0PHl+ciIW38DPUHcHcwlYykjYrwWXbTUFvtdeNdlo3f5gClqhMog4rZvU20WYas1T9ELADeB8z5CycWAKYAD7FGP4BxnBvrwfFTtI08DHgHeBxzLPcRcGqqzkncbAPfxMzHO2mQsvw/Atv0E+fkVDOBwAAAABJRU5ErkJggg==
