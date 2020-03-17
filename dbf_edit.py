from dbfpy import dbf
import numpy as np
# from dbfpy import *

def generateElevPolygon():
	# for i in range(94):
	# 	rec = db[i]
	# 	if rec[0] == "Uplands":
	# 		rec["ELEVATION"] = 1500
	# 		rec.store()
	# 		del rec
	# 	else:
	# 		rec["ELEVATION"] += np.random.rand()*100
	# 		rec.store()
	# 		del rec
	# 		# print("Nothing")

	db = dbf.Dbf("init_topo_polygon/data/Original/Paleotopo_P100.dbf")
	polygon_type = []
	polygon_elev = np.zeros(shape = (len(db),1))

	for i,rec in enumerate(db):
		polygon_type.append(rec[0])
		polygon_elev[i] = rec[1] 

	np.savetxt('init_topo_polygon/polygon_elev.txt', polygon_elev, fmt='%1.1f' )

	with open('init_topo_polygon/polygon_type.txt', 'w') as f:
		for item in polygon_type:
			f.write("%s\n" % item)

def edit_DBF():
	
	# polygon_elev = np.loadtxt('polygon_elev.txt')	
	# with open('polygon_type.txt') as f:
 #    	polygon_type = f.read().splitlines()

 #    print('polygon_elev.shape',polygon_elev.shape)
 #    print(set(polygon_type),len(set(polygon_type)))

	db = dbf.Dbf("init_topo_polygon/data/Original/Paleotopo_P100.dbf")
	
	for i,rec in enumerate(db):
		
		if rec[0] == "Uplands":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Land unclassified":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Land":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Marine shallow":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Land erosional":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Marine abyssal":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Fluvial":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Coastal depositional paralic":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Marine very shallow":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Fluvial-lacustrine":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		elif rec[0] == "Lacustrine":
			rec["ELEVATION"] += np.random.rand()*100
			rec.store()
			del rec
		else:
			pass
			# Do Nothing
	db.close()


def main():
	generateElevPolygon()
	# edit_DBF()

if __name__ == "__main__": main()