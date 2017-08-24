import hpastewebplugins

def webPack(asciiText):
	packid=None
	for cls in hpastewebplugins.pluginClassList:
		try:
			packer=cls()
			packid=packer.webPackData(asciiText)
			break
		except Exception as e:
			print("error: %s"%e.message)
			print("failed to pack with plugin %s, looking for alternatives..."%cls.__name__)
			continue
	if(packid is None):
		print("all web packing methods failed, sorry :(")
		raise RuntimeError("couldnt web pack data")

	return '@'.join((packid,cls.__name__))

def webUnpack(wid):
	if (wid.count('@') != 1): raise RuntimeError('given wid is not a valid wid')
	(id, cname) = wid.split('@')

	pretendents=[x for x in hpastewebplugins.pluginClassList if x.__name__==cname]
	if(len(pretendents)==0):
		raise RuntimeError("No plugins that can process this wid found")

	asciiText=None
	for cls in pretendents:
		try:
			unpacker=cls()
			asciiText=unpacker.webUnpackData(id)
			break
		except:
			print("error: %s" % e.message)
			print("keep trying...")
			continue
	if(asciiText is None):
		raise("couldnt web unpack data")
	return asciiText