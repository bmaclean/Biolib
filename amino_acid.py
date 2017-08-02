from enum import Enum


class AminoAcid(Enum):

    val = ("Valine")
    val.set_abbrv("V")
    val.set_structure("CC(C)[C@@H](C(=O)O)N")  # @@ indicated L-enantiomer
    val.set_mol_mass(117.15)
    val.set_iso_point(6.0)
    val.set_spec_rotation(22.9)
    val.set_melting_point(298.0)

    tyr = ("Tyrosine")
    tyr.set_abbrv("Y")
    tyr.set_structure("C1=CC(=CC=C1C[C@@H](C(=O)O)N)O")
    tyr.set_mol_mass(181.19)
    tyr.set_iso_point(5.66)
    tyr.set_spec_rotation(-10.6)
    tyr.set_melting_point(343.0)

    def __init__(self, name, abbrv, structure, mol_mass, iso_point, spec_rotation, melting_point):
        # IUPAC AA name
        self.name = name
        # 1-letter IUPAC code
        self.abbrv = None
        # AA SMILES structure
        self.structure = None
        # AA molecular mass in g/mol
        self.mol_mass = None
        # AA isoelectric point
        self.iso_point = None
        # AA specific rotation at 23deg C
        self.spec_rotation = None
        # AA melting point in C
        self.melting_point = None
        # frequency of occurrence
        self.freq = None

    def set_abbrv(self, abbrv):
        self.abbrv = abbrv

    def set_structure(self, structure):
        self.structure = structure

    def set_mol_mass(self, mol_mass):
        self.mol_mass = mol_mass

    def set_iso_point(self, iso_point):
        self.iso_point = iso_point

    def set_spec_rotation(self, spec_rotation):
        self.spec_rotation = spec_rotation

    def set_melting_point(self, melting_point):
        self.melting_point = melting_point

    def set_frequency(self, freq):
        self.freq = freq


# Use AminoAcid class to define valine:
val = AminoAcid("Valine")
val.set_abbrv("V")
val.set_structure("CC(C)[C@@H](C(=O)O)N")   # @@ indicated L-enantiomer
val.set_mol_mass(117.15)
val.set_iso_point(6.0)
val.set_spec_rotation(22.9)
val.set_melting_point(298.0)

# Use AminoAcid class to define tyrosine:
tyr = AminoAcid("Tyrosine")
tyr.set_abbrv("Y")
tyr.set_structure("C1=CC(=CC=C1C[C@@H](C(=O)O)N)O")
tyr.set_mol_mass(181.19)
tyr.set_iso_point(5.66)
tyr.set_spec_rotation(-10.6)
tyr.set_melting_point(343.0)


