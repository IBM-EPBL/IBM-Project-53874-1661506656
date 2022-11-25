pwd
Out[1]:
'/home/wsuser/work'
In [2]:
!pip install tensorflow==2.7.1
Collecting tensorflow==2.7.1
 Downloading tensorflow-2.7.1-cp39-cp39-manylinux2010_x86_64.whl (495.2 MB)
 |████████████████████████████████| 495.2 MB 29 kB/s s eta 0:00:01
Requirement already satisfied: h5py>=2.9.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (3.2.1)
Requirement already satisfied: wheel<1.0,>=0.32.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (0.37.0)
Requirement already satisfied: numpy>=1.14.5 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (1.20.3)
Requirement already satisfied: six>=1.12.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (1.15.0)
Requirement already satisfied: google-pasta>=0.1.1 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (0.2.0)
Requirement already satisfied: typing-extensions>=3.6.6 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorflow==2.7.1) (4.1.1)
Requirement already satisfied: astunparse>=1.6.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (1.6.3)
Requirement already satisfied: keras-preprocessing>=1.1.1 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorflow==2.7.1) (1.1.2)
Collecting libclang>=9.0.1
 Downloading libclang-14.0.6-py2.py3-none-manylinux2010_x86_64.whl (14.1 MB)
 |████████████████████████████████| 14.1 MB 29.9 MB/s eta 0:00:01
Requirement already satisfied: keras<2.8,>=2.7.0rc0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorflow==2.7.1) (2.7.0)
Requirement already satisfied: termcolor>=1.1.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (1.1.0)
Requirement already satisfied: absl-py>=0.4.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (0.12.0)
Requirement already satisfied: tensorflow-estimator<2.8,~=2.7.0rc0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorflow==2.7.1) (2.7.0)
Requirement already satisfied: wrapt>=1.11.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (1.12.1)
Requirement already satisfied: gast<0.5.0,>=0.2.1 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (0.4.0)
Requirement already satisfied: flatbuffers<3.0,>=1.12 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorflow==2.7.1) (2.0)
Requirement already satisfied: grpcio<2.0,>=1.24.3 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (1.42.0)
Requirement already satisfied: tensorboard~=2.6 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (2.7.0)
Requirement already satisfied: opt-einsum>=2.3.2 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (3.3.0)
Requirement already satisfied: protobuf>=3.9.2 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorflow==2.7.1) (3.19.1)
Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.21.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorflow==2.7.1) (0.23.1)
Requirement already satisfied: werkzeug>=0.11.15 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.1) 
(2.0.2)
Requirement already satisfied: markdown>=2.6.8 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.1) 
(3.3.3)
Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorboard~=2.6->tensorflow==2.7.1) (0.4.4)
Requirement already satisfied: requests<3,>=2.21.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.1) 
(2.26.0)
Requirement already satisfied: tensorboard-plugin-wit>=1.6.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorboard~=2.6->tensorflow==2.7.1) (1.6.0)
Requirement already satisfied: google-auth<3,>=1.6.3 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorboard~=2.6->tensorflow==2.7.1) (1.23.0)
Requirement already satisfied: tensorboard-data-server<0.7.0,>=0.6.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
tensorboard~=2.6->tensorflow==2.7.1) (0.6.1)
Requirement already satisfied: setuptools>=41.0.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.1) 
(58.0.4)
Requirement already satisfied: pyasn1-modules>=0.2.1 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from googleauth<3,>=1.6.3->tensorboard~=2.6->tensorflow==2.7.1) (0.2.8)
Requirement already satisfied: rsa<5,>=3.1.4 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from google-auth<3,>=1.6.3-
>tensorboard~=2.6->tensorflow==2.7.1) (4.7.2)
Requirement already satisfied: cachetools<5.0,>=2.0.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from googleauth<3,>=1.6.3->tensorboard~=2.6->tensorflow==2.7.1) (4.2.2)
Requirement already satisfied: requests-oauthlib>=0.7.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from google-authoauthlib<0.5,>=0.4.1->tensorboard~=2.6->tensorflow==2.7.1) (1.3.0)
Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from pyasn1-
modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow==2.7.1) 
(0.4.8)
Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from requests<3,>=2.21.0->tensorboard~=2.6-
>tensorflow==2.7.1) (2022.9.24)
Requirement already satisfied: charset-normalizer~=2.0.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
requests<3,>=2.21.0->tensorboard~=2.6->tensorflow==2.7.1) (2.0.4)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
requests<3,>=2.21.0->tensorboard~=2.6->tensorflow==2.7.1) (1.26.7)
Requirement already satisfied: idna<4,>=2.5 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from requests<3,>=2.21.0->tensorboard~=2.6-
>tensorflow==2.7.1) (3.3)
Requirement already satisfied: oauthlib>=3.0.0 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from requests-oauthlib>=0.7.0->google-authoauthlib<0.5,>=0.4.1->tensorboard~=2.6->tensorflow==2.7.1) (3.2.1)
Installing collected packages: libclang, tensorflow
 Attempting uninstall: tensorflow
 Found existing installation: tensorflow 2.7.2
 Uninstalling tensorflow-2.7.2:
 Successfully uninstalled tensorflow-2.7.2
Successfully installed libclang-14.0.6 tensorflow-2.7.1
In [3]:
from tensorflow.keras.preprocessing.image import ImageDataGenerator
2022-11-09 13:34:01.056483: W 
tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load 
dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open 
shared object file: No such file or directory; LD_LIBRARY_PATH: 
/opt/ibm/dsdriver/lib:/opt/oracle/lib:/opt/conda/envs/Python3.9/lib/python3.9/site-packages/tensorflow
In [4]:
# Training Datagen
train_datagen =
ImageDataGenerator(rescale=1/255,zoom_range=0.2,horizontal_flip=True,vertical
_flip=False)
# Testing Datagen
test_datagen = ImageDataGenerator(rescale=1/255)
In [5]:
import os, types
import pandas as pd
from botocore.client import Config
import ibm_boto3
def __iter__(self): return 0
# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It 
includes your credentials.
# You might want to remove those credentials before you share the notebook.
cos_client = ibm_boto3.client(service_name='s3',
 ibm_api_key_id='mT4yG1S3H9nBBV3UAwsgkb5FH89r-koWMhH4gnnWTjhN',
 ibm_auth_endpoint="https://iam.cloud.ibm.com/oidc/token",
 config=Config(signature_version='oauth'),
 endpoint_url='https://s3.private.us.cloud-objectstorage.appdomain.cloud')
bucket = 'imageclassification-donotdelete-pr-u5ptdjnvogkjw6'
object_key = 'Dataset.zip'
streaming_body_2 = cos_client.get_object(Bucket=bucket, 
Key=object_key)['Body']
# Your data file was loaded into a botocore.response.StreamingBody object.
# Please read the documentation of ibm_boto3 and pandas to learn more about 
the possibilities to load the data.
# ibm_boto3 documentation: https://ibm.github.io/ibm-cos-sdk-python/
# pandas documentation: http://pandas.pydata.org/
In [7]:
# Unzip the Dataset Zip File
from io import BytesIO
import zipfile
unzip = zipfile.ZipFile(BytesIO(streaming_body_2.read()), 'r')
file_paths = unzip.namelist()
for path in file_paths:
 unzip.extract(path)
In [8]:
%%bash
ls Dataset
test_set
training_set
In [9]:
# Training Dataset
x_train=train_datagen.flow_from_directory(r'/home/wsuser/work/Dataset/trainin
g_set',target_size=(64,64), class_mode='categorical',batch_size=900)
# Testing Dataset
x_test=test_datagen.flow_from_directory(r'/home/wsuser/work/Dataset/test_set'
,target_size=(64,64), class_mode='categorical',batch_size=900)
Found 15750 images belonging to 9 classes.
Found 2250 images belonging to 9 classes.
In [10]:
print("Len x-train : ", len(x_train))
print("Len x-test : ", len(x_test))
Len x-train : 18
Len x-test : 3
In [11]:
# The Class Indices in Training Dataset
x_train.class_indices
Out[11]:
{'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
Model Creation
In [12]:
# Importing Libraries
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D,MaxPooling2D,Flatten,Dense
In [13]:
# Creating Model
model=Sequential()
2022-11-09 13:34:42.826857: W 
tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load 
dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared 
object file: No such file or directory; LD_LIBRARY_PATH: 
/opt/ibm/dsdriver/lib:/opt/oracle/lib:/opt/conda/envs/Python3.9/lib/python3.9/site-packages/tensorflow
2022-11-09 13:34:42.826944: W 
tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: 
UNKNOWN ERROR (303)
In [14]:
# Adding Layers
model.add(Convolution2D(32,(3,3),activation='relu',input_shape=(64,64,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
# Adding Hidden Layers
model.add(Dense(300,activation='relu'))
model.add(Dense(150,activation='relu'))
# Adding Output Layer
model.add(Dense(9,activation='softmax'))
In [15]:
# Compiling the Model
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accu
racy'])
In [16]:
# Fitting the Model Generator
model.fit_generator(x_train,steps_per_epoch=len(x_train),epochs=10,validation
_data=x_test,validation_steps=len(x_test))
/tmp/wsuser/ipykernel_164/1042518445.py:2: UserWarning: `Model.fit_generator` 
is deprecated and will be removed in a future version. Please use 
`Model.fit`, which supports generators.
 
model.fit_generator(x_train,steps_per_epoch=len(x_train),epochs=10,validation
_data=x_test,validation_steps=len(x_test))
Epoch 1/10
18/18 [==============================] - 74s 4s/step - loss: 1.3704 -
accuracy: 0.5568 - val_loss: 0.4835 - val_accuracy: 0.8809
Epoch 2/10
18/18 [==============================] - 74s 4s/step - loss: 0.3403 -
accuracy: 0.8987 - val_loss: 0.2734 - val_accuracy: 0.9187
Epoch 3/10
18/18 [==============================] - 74s 4s/step - loss: 0.1527 -
accuracy: 0.9580 - val_loss: 0.2531 - val_accuracy: 0.9444
Epoch 4/10
18/18 [==============================] - 75s 4s/step - loss: 0.0862 -
accuracy: 0.9771 - val_loss: 0.2031 - val_accuracy: 0.9622
Epoch 5/10
18/18 [==============================] - 73s 4s/step - loss: 0.0526 -
accuracy: 0.9865 - val_loss: 0.2335 - val_accuracy: 0.9640
Epoch 6/10
18/18 [==============================] - 75s 4s/step - loss: 0.0343 -
accuracy: 0.9923 - val_loss: 0.2349 - val_accuracy: 0.9724
Epoch 7/10
18/18 [==============================] - 73s 4s/step - loss: 0.0252 -
accuracy: 0.9944 - val_loss: 0.2387 - val_accuracy: 0.9738
Epoch 8/10
18/18 [==============================] - 74s 4s/step - loss: 0.0176 -
accuracy: 0.9962 - val_loss: 0.2614 - val_accuracy: 0.9693
Epoch 9/10
18/18 [==============================] - 74s 4s/step - loss: 0.0152 -
accuracy: 0.9968 - val_loss: 0.2669 - val_accuracy: 0.9724
Epoch 10/10
18/18 [==============================] - 74s 4s/step - loss: 0.0145 -
accuracy: 0.9970 - val_loss: 0.2757 - val_accuracy: 0.9747
Out[16]:
Saving the Model
In [17]:
model.save('aslpng1.h5')
# Current accuracy is 0.8154
In [18]:
# Convert the Saved Model to a Tar Compressed Format
!tar -zcvf trainedModel.tgz aslpng1.h5
aslpng1.h5
In [19]:
%%bash
ls -ll
total 210184
-rw-rw---- 1 wsuser wscommon 111324760 Nov 9 13:49 aslpng1.h5
drwxrwx--- 4 wsuser wscommon 4096 Nov 9 13:34 Dataset
-rw-rw---- 1 wsuser wscommon 103895281 Nov 9 13:49 trainedModel.tgz
Watson Machine Learning
In [20]:
!pip install watson-machine-learning-client --upgrade
Collecting watson-machine-learning-client
 Downloading watson_machine_learning_client-1.0.391-py3-none-any.whl (538 
kB)
 |████████████████████████████████| 538 kB 17.4 MB/s eta 0:00:01
Requirement already satisfied: lomond in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from watson-machine-learning-client) (0.3.3)
Requirement already satisfied: ibm-cos-sdk in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from watson-machine-learning-client) 
(2.11.0)
Requirement already satisfied: tqdm in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from watson-machine-learning-client) 
(4.62.3)
Requirement already satisfied: boto3 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from watson-machine-learning-client) 
(1.18.21)
Requirement already satisfied: pandas in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from watson-machine-learning-client) (1.3.4)
Requirement already satisfied: tabulate in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from watson-machine-learning-client) (0.8.9)
Requirement already satisfied: requests in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from watson-machine-learning-client) 
(2.26.0)
Requirement already satisfied: certifi in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from watson-machine-learning-client) 
(2022.9.24)
Requirement already satisfied: urllib3 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from watson-machine-learning-client) 
(1.26.7)
Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from boto3->watsonmachine-learning-client) (0.10.0)
Requirement already satisfied: s3transfer<0.6.0,>=0.5.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from boto3->watsonmachine-learning-client) (0.5.0)
Requirement already satisfied: botocore<1.22.0,>=1.21.21 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from boto3->watsonmachine-learning-client) (1.21.41)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from 
botocore<1.22.0,>=1.21.21->boto3->watson-machine-learning-client) (2.8.2)
Requirement already satisfied: six>=1.5 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from python-dateutil<3.0.0,>=2.1-
>botocore<1.22.0,>=1.21.21->boto3->watson-machine-learning-client) (1.15.0)
Requirement already satisfied: ibm-cos-sdk-s3transfer==2.11.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from ibm-cos-sdk-
>watson-machine-learning-client) (2.11.0)
Requirement already satisfied: ibm-cos-sdk-core==2.11.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from ibm-cos-sdk-
>watson-machine-learning-client) (2.11.0)
Requirement already satisfied: idna<4,>=2.5 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from requests->watson-machine-learningclient) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in 
/opt/conda/envs/Python-3.9/lib/python3.9/site-packages (from requests-
>watson-machine-learning-client) (2.0.4)
Requirement already satisfied: pytz>=2017.3 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from pandas->watson-machine-learning-client) 
(2021.3)
Requirement already satisfied: numpy>=1.17.3 in /opt/conda/envs/Python3.9/lib/python3.9/site-packages (from pandas->watson-machine-learning-client) 
(1.20.3)
Installing collected packages: watson-machine-learning-client
Successfully installed watson-machine-learning-client-1.0.391
In [22]:
from ibm_watson_machine_learning import APIClient
wml_credentials = {
 "url": "https://us-south.ml.cloud.ibm.com",
 "apikey": "4y7eNmzaeDsCxie0E5b-PACwiQldF2Ock7lM6VAd28Fb"
}
client = APIClient(wml_credentials)
Save to Deployment Space
In [23]:
def guid_from_space_name(client, space_name):
 space = client.spaces.get_details()
 return (next(item for item in space['resources'] if
item['entity']["name"] == space_name)['metadata']['id'])
In [24]:
space_uid = guid_from_space_name(client, 'model')
print("Space UID : ", space_uid)
Space UID : 7ea8348c-8baa-4f9a-bac8-f21015c4bc86
In [25]:
client.set.default_space(space_uid)
Out[25]:
'SUCCESS'
In [26]:
client.software_specifications.list()
----------------------------- ------------------------------------ ----
NAME ASSET_ID TYPE
default_py3.6 0062b8c9-8b7d-44a0-a9b9-46c416adcbd9 base
kernel-spark3.2-scala2.12 020d69ce-7ac1-5e68-ac1a-31189867356a base
pytorch-onnx_1.3-py3.7-edt 069ea134-3346-5748-b513-49120e15d288 base
scikit-learn_0.20-py3.6 09c5a1d0-9c1e-4473-a344-eb7b665ff687 base
spark-mllib_3.0-scala_2.12 09f4cff0-90a7-5899-b9ed-1ef348aebdee base
pytorch-onnx_rt22.1-py3.9 0b848dd4-e681-5599-be41-b5f6fccc6471 base
ai-function_0.1-py3.6 0cdb0f1e-5376-4f4d-92dd-da3b69aa9bda base
shiny-r3.6 0e6e79df-875e-4f24-8ae9-62dcc2148306 base
tensorflow_2.4-py3.7-horovod 1092590a-307d-563d-9b62-4eb7d64b3f22 base
pytorch_1.1-py3.6 10ac12d6-6b30-4ccd-8392-3e922c096a92 base
tensorflow_1.15-py3.6-ddl 111e41b3-de2d-5422-a4d6-bf776828c4b7 base
runtime-22.1-py3.9 12b83a17-24d8-5082-900f-0ab31fbfd3cb base
scikit-learn_0.22-py3.6 154010fa-5b3b-4ac1-82af-4d5ee5abbc85 base
default_r3.6 1b70aec3-ab34-4b87-8aa0-a4a3c8296a36 base
pytorch-onnx_1.3-py3.6 1bc6029a-cc97-56da-b8e0-39c3880dbbe7 base
kernel-spark3.3-r3.6 1c9e5454-f216-59dd-a20e-474a5cdf5988 base
pytorch-onnx_rt22.1-py3.9-edt 1d362186-7ad5-5b59-8b6c-9d0880bde37f base
tensorflow_2.1-py3.6 1eb25b84-d6ed-5dde-b6a5-3fbdf1665666 base
spark-mllib_3.2 20047f72-0a98-58c7-9ff5-a77b012eb8f5 base
tensorflow_2.4-py3.8-horovod 217c16f6-178f-56bf-824a-b19f20564c49 base
runtime-22.1-py3.9-cuda 26215f05-08c3-5a41-a1b0-da66306ce658 base
do_py3.8 295addb5-9ef9-547e-9bf4-92ae3563e720 base
autoai-ts_3.8-py3.8 2aa0c932-798f-5ae9-abd6-15e0c2402fb5 base
tensorflow_1.15-py3.6 2b73a275-7cbf-420b-a912-eae7f436e0bc base
kernel-spark3.3-py3.9 2b7961e2-e3b1-5a8c-a491-482c8368839a base
pytorch_1.2-py3.6 2c8ef57d-2687-4b7d-acce-01f94976dac1 base
spark-mllib_2.3 2e51f700-bca0-4b0d-88dc-5c6791338875 base
pytorch-onnx_1.1-py3.6-edt 32983cea-3f32-4400-8965-dde874a8d67e base
spark-mllib_3.0-py37 36507ebe-8770-55ba-ab2a-eafe787600e9 base
spark-mllib_2.4 390d21f8-e58b-4fac-9c55-d7ceda621326 base
xgboost_0.82-py3.6 39e31acd-5f30-41dc-ae44-60233c80306e base
pytorch-onnx_1.2-py3.6-edt 40589d0e-7019-4e28-8daa-fb03b6f4fe12 base
default_r36py38 41c247d3-45f8-5a71-b065-8580229facf0 base
autoai-ts_rt22.1-py3.9 4269d26e-07ba-5d40-8f66-2d495b0c71f7 base
autoai-obm_3.0 42b92e18-d9ab-567f-988a-4240ba1ed5f7 base
pmml-3.0_4.3 493bcb95-16f1-5bc5-bee8-81b8af80e9c7 base
spark-mllib_2.4-r_3.6 49403dff-92e9-4c87-a3d7-a42d0021c095 base
xgboost_0.90-py3.6 4ff8d6c2-1343-4c18-85e1-689c965304d3 base
pytorch-onnx_1.1-py3.6 50f95b2a-bc16-43bb-bc94-b0bed208c60b base
autoai-ts_3.9-py3.8 52c57136-80fa-572e-8728-a5e7cbb42cde base
spark-mllib_2.4-scala_2.11 55a70f99-7320-4be5-9fb9-9edb5a443af5 base
spark-mllib_3.0 5c1b0ca2-4977-5c2e-9439-ffd44ea8ffe9 base
autoai-obm_2.0 5c2e37fa-80b8-5e77-840f-d912469614ee base
spss-modeler_18.1 5c3cad7e-507f-4b2a-a9a3-ab53a21dee8b base
cuda-py3.8 5d3232bf-c86b-5df4-a2cd-7bb870a1cd4e base
autoai-kb_3.1-py3.7 632d4b22-10aa-5180-88f0-f52dfb6444d7 base
pytorch-onnx_1.7-py3.8 634d3cdc-b562-5bf9-a2d4-ea90a478456b base
spark-mllib_2.3-r_3.6 6586b9e3-ccd6-4f92-900f-0f8cb2bd6f0c base
tensorflow_2.4-py3.7 65e171d7-72d1-55d9-8ebb-f813d620c9bb base
spss-modeler_18.2 687eddc9-028a-4117-b9dd-e57b36f1efa5 base
----------------------------- ------------------------------------ ----
Note: Only first 50 records were displayed. To display more use 'limit' 
parameter.
In [27]:
software_spec_uid =
client.software_specifications.get_uid_by_name("tensorflow_rt22.1-py3.9")
software_spec_uid
Out[27]:
'acd9c798-6974-5d2f-a657-ce06e986df4d'
In [31]:
model_details = client.repository.store_model(model='trainedModel.tgz', 
meta_props={
 client.repository.ModelMetaNames.NAME: "CNN",
 client.repository.ModelMetaNames.SOFTWARE_SPEC_UID: software_spec_uid,
 client.repository.ModelMetaNames.TYPE: "tensorflow_2.7"})
model_id = client.repository.get_model_id(model_details)
In [32]:
model_id
Out[32]:
'eec72d86-8ba8-46cc-8588-c9ff4bf89c85'
In [35]:
client.repository.download(model_id,'aslpng1.tar.gz')
Successfully saved model content to file: 'aslpng1.tar.gz'
Out[35]:
'/home/wsuser/work/aslpng1.tar.gz'
In [ ]