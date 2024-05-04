import sys
import os
from PIL import Image
from datetime import datetime
import hashlib


print("\n  METS Structure: AMDSEC, FILESEC for TIFF, JP2, PDF, ALTO\n")

# METS XML Structures Creation
# AMDSEC for TIFF Image
# FileSec for TIFF, JP2, ALTO, PDF

filepath1 = input("  Enter the File path: ")

filepath = filepath1 + "\\"

filelist = os.path.isdir(filepath)

if os.path.exists(filepath + '01_amdsec.mets'):
	os.remove(filepath + '01_amdsec.mets')
if os.path.exists(filepath + '02_filesec-tiff.mets'):
	os.remove(filepath + '02_filesec-tiff.mets')
if os.path.exists(filepath + '03_filesec-jp2.mets'):
	os.remove(filepath + '03_filesec-jp2.mets')
if os.path.exists(filepath + '04_filesec-pdf.mets'):
	os.remove(filepath + '04_filesec-pdf.mets')
if os.path.exists(filepath + '05_filesec-alto.mets'):
	os.remove(filepath + '05_filesec-alto.mets')

amd_count = 0
tiff_count = 0
jp2_count = 0
pdf_count = 0
alto_count = 0

for fname in os.listdir(filepath):
		if not fname.endswith(".tif"):
			continue
		path = os.path.join(filepath, fname) 
		print("  File: " + fname)
		amd_count += 1
		seq1 = str(amd_count).zfill(5)
		Image.MAX_IMAGE_PIXELS = 933120000
		img = Image.open(path)    
		width = str(img.width)
		height = str(img.height)
		img_dpi = str(int(img.info['dpi'][0]))
		img_compr = str(img.info['compression'])
		if img_compr == "raw":
		   comp1 = "Uncompressed"
		else:
		   comp1 = "LZW"
		filesize = str(os.path.getsize(path))
		amdsec = "<amdSec ID=" + "\"" + "IMGPARAM" + seq1 + "\"" + ">" + "\n" + "<techMD ID=" + "\"" + "IMGPARAM" + seq1 + "TECHMD" + "\"" + ">" + "\n" + "<mdWrap MDTYPE=" + "\"" + "NISOIMG" + "\"" + ">" + "\n" + "<xmlData>" + "\n" + "<mix:mix>" + "\n" + "<mix:BasicDigitalObjectInformation>" + "\n" + "<mix:ObjectIdentifier>" + "\n" + "<mix:objectIdentifierType>Local File Reference</mix:objectIdentifierType>" + "\n" + "<mix:objectIdentifierValue>" + fname + "</mix:objectIdentifierValue>" + "\n" + "</mix:ObjectIdentifier>" + "\n" + "<mix:fileSize>" + filesize + "</mix:fileSize>" + "\n" + "<mix:FormatDesignation>" + "\n" + "<mix:formatName>image/tiff</mix:formatName>" + "\n" + "<mix:formatVersion>TIFF 6.0</mix:formatVersion>" + "\n" + "</mix:FormatDesignation>" + "\n" + "<mix:byteOrder>little endian</mix:byteOrder>" + "\n" + "<mix:Compression>" + "\n" + "<mix:compressionScheme>" + comp1 + "</mix:compressionScheme>" + "\n" + "</mix:Compression>" + "\n" + "</mix:BasicDigitalObjectInformation>" + "\n" + "<mix:BasicImageInformation>" + "\n" + "<mix:BasicImageCharacteristics>" + "\n" + "<mix:imageWidth>" + width + "</mix:imageWidth>" + "\n" + "<mix:imageHeight>" + height + "</mix:imageHeight>" + "\n" + "</mix:BasicImageCharacteristics>" + "\n" + "</mix:BasicImageInformation>" + "\n" + "<mix:ImageCaptureMetadata>" + "\n" + "<mix:SourceInformation>" + "\n" + "<mix:sourceType>Newspaper</mix:sourceType>" + "\n" + "<mix:SourceID>" + "\n" + "<mix:sourceIDType>Volume identifier</mix:sourceIDType>" + "\n" + "<mix:sourceIDValue>" + "[VOLUME IDENTIFIER]" + "</mix:sourceIDValue>" + "\n" + "</mix:SourceID>" + "\n" + "</mix:SourceInformation>" + "\n" + "<mix:GeneralCaptureInformation>" + "\n" + "<mix:imageProducer>Ninestars Information Technologies Pvt Ltd</mix:imageProducer>" + "\n" + "</mix:GeneralCaptureInformation>" + "\n" + "<mix:ScannerCapture>" + "\n" + "<mix:scannerManufacturer>" + "[SCANNER NAME]" + "</mix:scannerManufacturer>" + "\n" + "<mix:ScannerModel>" + "\n" + "<mix:scannerModelName>" + "[SCANNER MODEL NAME]" + "</mix:scannerModelName>" + "\n" + "</mix:ScannerModel>" + "\n" + "<mix:MaximumOpticalResolution>" + "\n" + "<mix:xOpticalResolution>" + img_dpi + "</mix:xOpticalResolution>" + "\n" + "<mix:yOpticalResolution>" + img_dpi + "</mix:yOpticalResolution>" + "\n" + "<mix:opticalResolutionUnit>in.</mix:opticalResolutionUnit>" + "\n" + "</mix:MaximumOpticalResolution>" + "\n" + "<mix:ScanningSystemSoftware>" + "\n" + "<mix:scanningSoftwareName>" + "[SCANNER SOFTWARE]" + "</mix:scanningSoftwareName>" + "\n" + "</mix:ScanningSystemSoftware>" + "\n" + "</mix:ScannerCapture>" + "\n" + "</mix:ImageCaptureMetadata>" + "\n" + "</mix:mix>" + "\n" + "</xmlData>" + "\n" + "</mdWrap>" + "\n" + "</techMD>" + "\n" + "</amdSec>" + "\n"
		text_file1 = filepath + "01_amdsec.mets"
		f = open(text_file1, "a+")           # "a+" means appending the all image properties one by one 
		f.write(str(amdsec))
		f.close()
print("\n  *****AMDSEC Completed*****\n")



for fname in os.listdir(filepath):
		if not fname.endswith(".tif"):
			continue
		path = os.path.join(filepath, fname) 
		print("  File: " + fname)
		tiff_count += 1
		seq2 = str(tiff_count).zfill(5)
		seq_val = str(tiff_count)
		Image.MAX_IMAGE_PIXELS = 933120000
		with open(path,"rb") as f:
			bytes = f.read() # read file as bytes
			md5_hash = hashlib.md5(bytes).hexdigest();
		filesize = str(os.path.getsize(path))
		c_time = os.path.getmtime(path)
		dt_c = datetime.fromtimestamp(c_time)
		date_val = dt_c.strftime('%Y-%m-%d' + "T" + '%H:%M:%S')

		tiff_filesec = "<file ID=" + "\"" + "IMG" + seq2  + "\"" + " CREATED="  + "\"" +  date_val  + "\"" +  " MIMETYPE="  + "\"" +  "image/tiff"  + "\"" +  " ADMID="  + "\"" +  "IMGPARAM" + seq2  + "\"" +  " SEQ="  + "\"" +  seq_val  + "\"" +  " GROUPID="  + "\"" +  seq_val  + "\"" +  " CHECKSUM="  + "\"" +  md5_hash + "\"" +  " CHECKSUMTYPE="  + "\"" +  "MD5"  + "\"" +  " SIZE="  + "\"" +  filesize  + "\"" +  ">" + "\n" + "<FLocat LOCTYPE="  + "\"" +  "URL"  + "\"" +  " xlink:href="  + "\"" +  fname  + "\"" + "/" + ">" + "\n" + "</file>" + "\n"
		text_file2 = filepath + "02_filesec-tiff.mets"
		f = open(text_file2, "a+")           # "a+" means appending the all image properties one by one 
		f.write(str(tiff_filesec))
		f.close()
print("\n  *****FileSec TIFF Completed*****\n")




for fname in os.listdir(filepath):
		if not fname.endswith(".jp2"):
			continue
		path = os.path.join(filepath, fname) 
		print("  File: " + fname)
		jp2_count += 1
		seq3 = str(jp2_count).zfill(5)
		seq_val = str(jp2_count)
		filesize = str(os.path.getsize(path))
		c_time = os.path.getmtime(path)
		dt_c = datetime.fromtimestamp(c_time)
		date_val = dt_c.strftime('%Y-%m-%d' + "T" + '%H:%M:%S')
		with open(path,"rb") as f:
			bytes = f.read() # read file as bytes
			md5_hash = hashlib.md5(bytes).hexdigest();
		jp2_filesec = "<file ID=" + "\"" + "JPG" + seq3  + "\"" + " CREATED="  + "\"" +  date_val  + "\"" +  " MIMETYPE="  + "\"" +  "image/jp2"  + "\"" +  " SEQ="  + "\"" +  seq_val  + "\"" +  " GROUPID="  + "\"" +  seq_val  + "\"" +  " CHECKSUM="  + "\"" +  md5_hash  + "\"" +  " CHECKSUMTYPE="  + "\"" +  "MD5"  + "\"" +  " SIZE="  + "\"" +  filesize  + "\"" +  ">" + "\n" + "<FLocat LOCTYPE="  + "\"" +  "URL"  + "\"" +  " xlink:href="  + "\"" +  fname  + "\""  + "/" +  ">" + "\n" + "</file>" + "\n"
		text_file3 = filepath + "03_filesec-jp2.mets"
		f = open(text_file3, "a+")           # "a+" means appending the all image properties one by one 
		f.write(str(jp2_filesec))
		f.close()
print("\n  *****FileSec JP2 Completed*****\n")




for fname in os.listdir(filepath):
		if not fname.endswith(".pdf"):
			continue
		path = os.path.join(filepath, fname) 
		print("  File: " + fname)
		pdf_count += 1
		seq4 = str(pdf_count).zfill(5)
		seq_val = str(pdf_count)
		filesize = str(os.path.getsize(path))
		c_time = os.path.getmtime(path)
		dt_c = datetime.fromtimestamp(c_time)
		date_val = dt_c.strftime('%Y-%m-%d' + "T" + '%H:%M:%S')
		with open(path,"rb") as f:
			bytes = f.read() # read file as bytes
			md5_hash = hashlib.md5(bytes).hexdigest();
		pdf_filesec = "<file ID=" + "\"" + "PAGEPDF" + seq4  + "\"" + " CREATED="  + "\"" +  date_val  + "\"" +  " MIMETYPE="  + "\"" +  "application/pdf"  + "\"" +  " SEQ="  + "\"" +  seq_val  + "\"" +  " GROUPID="  + "\"" +  seq_val  + "\"" +  " CHECKSUM="  + "\"" +  md5_hash  + "\"" +  " CHECKSUMTYPE="  + "\"" +  "MD5"  + "\"" +  " SIZE="  + "\"" +  filesize  + "\"" +  ">" + "\n" + "<FLocat LOCTYPE="  + "\"" +  "URL"  + "\"" +  " xlink:href="  + "\"" +  fname  + "\""  + "/" +  ">" + "\n" + "</file>" + "\n"
		text_file4 = filepath + "04_filesec-pdf.mets"
		f = open(text_file4, "a+")           # "a+" means appending the all image properties one by one 
		f.write(str(pdf_filesec))
		f.close()
print("\n  *****FileSec PDF Completed*****\n")




for fname in os.listdir(filepath):
		if not fname.endswith(".xml"):
			continue
		path = os.path.join(filepath, fname) 
		print("  File: " + fname)
		alto_count += 1
		seq5 = str(alto_count).zfill(5)
		seq_val = str(alto_count)
		filesize = str(os.path.getsize(path))
		c_time = os.path.getmtime(path)
		dt_c = datetime.fromtimestamp(c_time)
		date_val = dt_c.strftime('%Y-%m-%d' + "T" + '%H:%M:%S')
		with open(path,"rb") as f:
			bytes = f.read() # read file as bytes
			md5_hash = hashlib.md5(bytes).hexdigest();
		alto_filesec = "<file ID=" + "\"" + "ALTO" + seq5 + "\"" + " CREATED="  + "\"" +  date_val  + "\"" +  " MIMETYPE="  + "\"" +  "text/xml"  + "\"" +  " SEQ="  + "\"" +  seq_val  + "\"" +  " GROUPID="  + "\"" +  seq_val  + "\"" +  " CHECKSUM="  + "\"" +  md5_hash  + "\"" +  " CHECKSUMTYPE="  + "\"" +  "MD5"  + "\"" +  " SIZE="  + "\"" +  filesize  + "\"" +  ">" + "\n" + "<FLocat LOCTYPE="  + "\"" +  "URL"  + "\"" +  " xlink:href="  + "\"" +  fname  + "\""  + "/" +   ">" + "\n" + "</file>" + "\n"
		text_file5 = filepath + "05_filesec-alto.mets"
		f = open(text_file5, "a+")
		f.write(str(alto_filesec))
		f.close()
print("\n  *****FileSec ALTO XML Completed*****\n")

