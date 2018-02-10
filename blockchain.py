#!/usr/bin/env python3

import hashlib

class Block:
	def __init__(self,text,letzterBlockHash):
		self.text = text
		self.letzterBlockHash = letzterBlockHash
		self.hash = self.makeBlockhash(self.text,self.letzterBlockHash)

	def __str__(self):
		return 'Block text=%s' % (self.text)

	def makeBlockhash(self,text,letzterBlockHash):
		BlockHash = hashlib.sha256()
		BlockHash.update(bytes(text,'utf8'))
		BlockHash.update(bytes(letzterBlockHash,'utf8'))
		return BlockHash.hexdigest()

class Blockchain:
	def __init__(self):
		self.chain = [Block('Genesis Block','')]

	def addBlock(self,text):
		self.chain.append(Block(text,self.chain[-1].hash))

	def verrify(self):
		for block in self.chain[1:]:
			if block.hash != block.makeBlockhash(block.text,block.letzterBlockHash):
				return False
			return True

	def printChain(self):
		for block in self.chain:
			print('letzter Hash:\n%s' % block.letzterBlockHash)
			print('Text:\n%s' % block.text)
			print('Hash:\n%s' % block.hash)
			print('----------------------')

if __name__ == '__main__':
	bc = Blockchain()
	bc.addBlock('Ein Test')
	bc.addBlock('Noch ein test')
	bc.addBlock('Noch ein test 2')
	bc.printChain()
	print(bc.verrify())

	bc.chain[1].text = 'Manipulation'
	bc.printChain()
	print(bc.verrify())

