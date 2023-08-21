# In-bed Multi-modal Human Dataset
This dataset recorded in-bed human subjects from multiple modality sensors including RGB, IR for pose estimation purpose. 
The data is collected in both a home setting and hospital setting environment named 'danaLab' and 'simLab' with 102 （73 male, 28 femaile) and 7 subjects (4 male 3 female) respectively. 
For each setting, subjects are requested to give 15 poses as wish in 3 general categories as supine, left lying and right lying. For each pose,data is collected from 3 cover conditions as uncover, cover1 and cover2.  

## File structure

Each subject is named with a numbered folder, with structure
```
[subjNumber]
|--	IR
|	|-- uncover
|	|-- cover1
|	|-- cover2
|-- RGB 
	...
|	|-- joints_gt_IR.mat
|	|-- joints_gt_RGB.mat
|	|-- align_PTr_IR.npy
|	|-- align_PTr_RGB.npy
|	|-- PMcali.npy
|	|-- ...	(auxliary ones)
```
Ohter files are auxilary ones during data generation which are not needed in training and testing. 

## Multi cover conditions 
Under each modality, there will be 3 cover conditions with corresponding same poses. 
 
## Modalities

`depthRaw` provides the raw depth data of uint16 of distance (mm) in camera. 
`IRraw` keeps the raw temperature data in (K) 
`PMarray` keeps the uint8 pressure raw reading from pressure map.
Exact pressure needs to be transferred to physical quantity (kPa) by scaling up which is providied in the calibration file.  

 To explore the data in convience, we also provide all image version of physical maps including  
`depth`,   `IR` and `PM` which can be viewed directly from a photo viewers. You can also employ them for a quick prototyping with models employing a conventional image (8bit) interface. 

For image conversion, the range is remapped to 0~255 as follows: 
`depth`:  0 ~ 3000 mm.  
`IR`:  20C ~ 40C 
`PM`: normalized based on individual map range. (in order to keep the low reading value in light weighted area).  



## Pose Definition
We follow the Leeds Sports Pose Dataset pose definition with 14 joints labeling, namely, 

`Right ankle
Right knee
Right hip
Left hip
Left knee
Left ankle
Right wrist
Right elbow
Right shoulder
Left shoulder
Left elbow
Left wrist
Thorax
Head top`

## Anotations 
`joints_gt_<modality>.mat` is the pose label file.  `RGB` and `IR` are manually labeled with physical paramter tuning strategy. Please refer our MICCAI'19 paper for details. Pose data from other modalities can be generated via the alignment homography provided. Possible bias could be introduced via the mapping process so we don't officially release them as 'unbiase' ground truth but you can easily generate them for your study as they are still semantically correct. 

The lable matrix `joints_gt_<modality>.mat` has the format  `<x,y,if_occluded>` x n_joints x n_subjects 

`PMcali.npy` provides the exact PM mapping scalars from raw array to actual pressure in kpa with size 3(cover_cases) x  45 (frms)



## Physique descriptor 
We also include a 10-dim tailor measure descriptor of each participant saved in `physiqueData.npy` at root of each settings. They are given in order: 
gender(1:male, 0:female), height	weight	bust	waist 	hip	right upper arm right lower arm	righ upper leg	right lower leg.  
where weight is in `kg` and tailor meausres is in `cm`. 

## Domain Alignment 
At beginning of each experiment session, we aign the all modalities with several weighted icons. The images of icons images are captured in all modalities and provided in raw form in this dataset in case you would like to have a customize re-calibration. They are given in name of `align_<mod>001.[png|npy]` depending on if that is image or deeper raw data. 

`align_PTr_<modality>.npy` saved the homography transformation matrix to reference frame which is PM in our case. To get transformation between other modalities for example RGB and IR, we can simply use `inv(H_RGB) * H_IR`. 
## Camera Parameters 
For camera parameters, 
RGB is recalibrated with checkbaords. 
Depth (kinect) is provided from factory setting. We have already transposed these parameters to cop with our vertical image settings, so you can use them directly wihtout transposing again:

The focal length(pixelized) and principle points are:
```
RGB:  
f_R = [902.6, 877.4]; 
c_R= [278.4,  525,1];

depth: 
c_d = [208.1, 259.7];     
f_d = [367.8, 367.8];
```

## Reference
@article{liu20120simultaneously, title={Simultaneously-Collected Multimodal Lying Pose Dataset: Towards In-Bed Human Pose Monitoring under Adverse Vision Conditions}, author={Liu, Shuangjun and Huang, Xiaofei and Fu, Nihang and Li, Cheng and Su, Zhongnan and Ostadabbas, Sarah}, journal={arXiv preprint arXiv:2008.08735}, year={2020} }

@inproceedings{liu2019seeing,
  title={Seeing under the cover: A physics guided learning approach for in-bed pose estimation},
  author={Liu, Shuangjun and Ostadabbas, Sarah},
  booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention},
  pages={236--245},
  year={2019},
  organization={Springer}
}

## Contact
Shuanjun Liu,
email: shuliu@ece.neu.edu

Sarah Ostadabbas, 
email: ostadabbas@ece.neu.edu

