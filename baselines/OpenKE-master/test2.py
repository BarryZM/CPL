import config
import models
import tensorflow as tf
import numpy as np
import os
#Input training files from benchmarks/FB15K/ folder.
con = config.Config()
#True: Input test files from the same folder.
con.set_in_path("./testsets/")
con.set_test_link_prediction(True)
con.set_test_triple_classification(True)
con.set_work_threads(4)
con.set_train_times(500)
con.set_nbatches(100)
con.set_alpha(0.1)
con.set_lmbda(0.0001)
con.set_bern(0)
con.set_dimension(100)
con.set_ent_neg_rate(1)
con.set_rel_neg_rate(0)
con.set_opt_method("Adagrad")

#Models will be exported via tf.Saver() automatically.
con.set_export_files("./res/model.vec.tf", 0)
#Model parameters will be exported to json files automatically.
con.set_out_files("./res/embedding.vec.json")
#Initialize experimental settings.
con.init()
#Set the knowledge embedding model
con.set_model(models.ComplEx)
#Train the model.
con.run()
#To test models after training needs "set_test_flag(True)".
con.test()