import unittest
from mesfonctions import addition, division, factorielle, est_pair, renverser_chaine

class TestFonctions(unittest.TestCase):

    # Test de la fonction addition
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

    # Test de la fonction division
    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(7, 2), 3.5)
        self.assertEqual(division(5, 0), "Erreur : division par zéro")
        self.assertAlmostEqual(division(1, 3), 0.3333333)

    # Test de la fonction factorielle
    def test_factorielle(self):
        self.assertEqual(factorielle(0), 1)
        self.assertEqual(factorielle(1), 1)
        self.assertEqual(factorielle(5), 120)
        self.assertEqual(factorielle(-3), "Erreur : nombre négatif")

    # Test de la fonction est_pair
    def test_est_pair(self):
        self.assertTrue(est_pair(2))
        self.assertTrue(est_pair(0))
        self.assertFalse(est_pair(3))
        self.assertTrue(est_pair(-4))
        self.assertFalse(est_pair(-7))

    # Test de la fonction renverser_chaine
    def test_renverser_chaine(self):
        self.assertEqual(renverser_chaine("bonjour"), "ruojnob")
        self.assertEqual(renverser_chaine(""), "")
        self.assertEqual(renverser_chaine("a"), "a")
        self.assertEqual(renverser_chaine("12345"), "54321")

if __name__ == '__main__':
    unittest.main()