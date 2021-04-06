%matplotlib inline
import os
from ktrain import vision as vis
import re
import glob
import cv2
import ktrain

pattern = r'([^/]+)_\d+_\d+.jpg$'
p = re.compile(pattern)
r = p.search('0_1_201701122135009013.jpg')
print(r.group(1))

DATADIR=r'C:\Users\mayurk\Desktop\Skin type images'

(train_data, test_data, preproc)=vis.images_from_fname(DATADIR, pattern=pattern,
                                                       is_regression=False,
                                                       random_state=42)

vis.print_image_regression_models()

model = vis.image_regression_model('pretrained_resnet50',train_data=train_data, val_data=test_data,metrics=['accuracy'])

learner = ktrain.get_learner(model=model, train_data=train_data, val_data= test_data, batch_size=64)

learner.fit_onecycle(1e-4, 11)

# learner.freeze(15)
# learner.fit_onecycle(1e-4, 11)

predictor = ktrain.get_predictor(learner.model, preproc)
