import numpy as np
from pprint import pprint as pp

np.set_printoptions(suppress=True)


class CONTCAR(object):
    def __init__(self, file="CONTCAR"):
        self.file = file
        self.raw_data = self.get_raw()
        self.comment = self.get_comment()
        self.symbols = self.get_symbols()
        self.counts = self.get_counts()
        self.symbols_complete = self.get_complete_symbols()
        self.natom = np.sum(self.counts)
        self.cell = self.get_cell()
        # remember contcar is always direct
        self.positions = self.get_positions()
        # converting internal coord to ang
        self.positions_ang = np.matmul(self.positions, self.cell)

    def get_comment(self):
        comment = self.raw_data[0].strip()
        return comment

    def get_symbols(self):
        symbols_line = self.raw_data[5].strip()
        return symbols_line.split()

    def get_counts(self):
        counts_line = self.raw_data[6].strip()
        return [int(a) for a in counts_line.split()]

    def get_complete_symbols(self):
        comp_syms = []
        for sym, count in zip(self.symbols, self.counts):
            for i in range(count):
                comp_syms.append(sym)
        return comp_syms

    def get_cell(self):
        cell = np.zeros((3, 3))
        for i in range(3):
            # cell line starts at 3nd line so 2+i
            cell[i] = [float(a) for a in self.raw_data[2+i].split()]
        return cell

    def get_positions(self):
        positions = np.zeros((self.natom, 3))
        for i in range(self.natom):
            # cell line starts at 3nd line so 2+i
            positions[i] = [float(a) for a in self.raw_data[8+i].split()]
        return positions

    def get_raw(self):
        with open(self.file) as fp:
            raw_data = fp.readlines()
        return raw_data

    def write_xyz(self, output_name="CONTCAR.xyz"):
        with open(output_name, "w") as fp:
            fp.write(f"{self.natom}\n")
            fp.write(f"{self.comment}\n")
            for sym, pos in zip(self.symbols_complete, self.positions_ang):
                fp.write(f"{sym:4} {pos[0]:12.6f} {pos[1]:12.6f} {pos[2]:12.6f}\n")

    def __str__(self):
        rep = f"AtomCount = {self.natom}\n"
        rep += f"Symbols = {self.symbols}\n"
        rep += f"Counts = {self.counts}\n"
        rep += f"Cell =\n{self.cell}"
        return rep


if __name__ == "__main__":
    mol = CONTCAR(file="CONTCAR")
    print(mol)
    mol.write_xyz()
