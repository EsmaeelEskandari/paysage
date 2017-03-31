from paysage import layers
from paysage import constraints
from paysage import penalties
from paysage import backends as be


# ----- CONSTRUCTORS ----- #

def test_Layer_creation():
    layers.Layer()

def test_Weights_creation():
    layers.Weights((8,5))

def test_Gaussian_creation():
    layers.GaussianLayer(8)

def test_Ising_creation():
    layers.IsingLayer(8)

def test_Bernoulli_creation():
    layers.BernoulliLayer(8)

def test_Exponential_creation():
    layers.ExponentialLayer(8)


# ----- BASE METHODS ----- #

def test_add_constraint():
    ly = layers.Weights((5,3))
    ly.add_constraint({'matrix': constraints.non_negative})

def test_enforce_constraints():
    ly = layers.Weights((5,3))
    ly.add_constraint({'matrix': constraints.non_negative})
    ly.enforce_constraints()

def test_add_penalty():
    ly = layers.Weights((5,3))
    p = penalties.l2_penalty(0.37)
    ly.add_penalty({'matrix': p})

def test_get_penalties():
    ly = layers.Weights((5,3))
    p = penalties.l2_penalty(0.37)
    ly.add_penalty({'matrix': p})
    ly.get_penalties()

def test_get_penalty_gradients():
    ly = layers.Weights((5,3))
    p = penalties.l2_penalty(0.37)
    ly.add_penalty({'matrix': p})
    ly.get_penalty_gradients()

def test_parameter_step():
    ly = layers.Weights((5,3))
    deltas = {'matrix': be.zeros_like(ly.W())}
    ly.parameter_step(deltas)

def test_get_base_config():
    ly = layers.Weights((5,3))
    ly.add_constraint({'matrix': constraints.non_negative})
    p = penalties.l2_penalty(0.37)
    ly.add_penalty({'matrix': p})
    ly.get_base_config()


# ----- Weights LAYER ----- #

def test_weights_derivative():
    ly = layers.Weights((5,3))
    p = penalties.l2_penalty(0.37)
    ly.add_penalty({'matrix': p})
    vis = be.ones((10,ly.shape[0]))
    hid = be.ones((10,ly.shape[1]))
    derivs = ly.derivatives(vis, hid)

def test_weights_energy():
    ly = layers.Weights((5,3))
    vis = be.ones((10,ly.shape[0]))
    hid = be.ones((10,ly.shape[1]))
    ly.energy(vis, hid)

def test_build_from_config():
    ly = layers.Weights((5,3))
    ly.add_constraint({'matrix': constraints.non_negative})
    p = penalties.l2_penalty(0.37)
    ly.add_penalty({'matrix': p})
    ly_new = layers.Weights.from_config(ly.get_config())


# ----- Gaussian LAYER ----- #
