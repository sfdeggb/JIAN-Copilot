import json 
import os 
import pathlib 
import argparse 

class convertData():
	def __init__(self,srcfile, despath):
		self.srcfile=srcfile
		self.despath=despath
	def convert(self):
		if not os.path.isfile(self.srcfile):
			print("the converted data file is not exists,please check the path is %s" % srcfile)
		if not os.path.exists(self.despath):
			# os.mkdir(self.despath)
			pass
		f= open(self.srcfile,"r",encoding="UTF-8")
		data=f.readlines()
		tardata={}
		datalist=[]
		k=0
		for i in (range(0,len(data))):
			if k == len(data):
				break
			else:
				question=data[k].split("+++$+++")
				question=question[2].strip()
				question.replace("\n", "")
				tardata['src_text']=question
				# print(data.index(line))
				answer=data[k+1]
				answer=answer.split("+++$+++")
				# print(answer)
				answer=answer[2].strip()
				answer.replace("\n", "")
				tardata["tgt_text"]=answer
				# print(tardata)
				# break
				datalist.append(tardata)
				tardata={}
				k=k+2
		f.close()
		return datalist 
	def write_data(self, data):
		with open(self.despath,"a", encoding="UTF-8") as f:
			for line in data:
				f.write(json.dumps(line,ensure_ascii=False))
				f.write("\n")
			f.close()
			print("writeing is done!")
   
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='请输入数据文件地址和储存地址')
    #nargs='+' at least there will be a param
    parser.add_argument('--srcpath',type=str,nargs='+',help="数据文件地址")
    parser.add_argument('--despath',type=str,nargs='+',help="存储地址")
    args=parser.parse_args()
    con=convertData(args.srcpath, args.despath)
    # con=convertData("D:/python/NLP-PY/UnilmChatchitRobot/data/egret_wenda_lines.txt", "D://ptb//nini.json")
    data=con.convert()
    con.write_data(data)
    
     
    
				