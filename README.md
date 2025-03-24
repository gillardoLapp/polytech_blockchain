# Blockchain Project

This project implements a simple blockchain without a Proof of Work (PoW). 

## Features
- Basic Blockchain with chaining of block
- Transaction system with public/private keys
- Simple Unit Tests

## How to run
1. Install dependencies: `pip install -r requirements.txt`
2. To run an example, run: `python main.py`


# Lab Polytech

## Objectives
    1. Understand the fundamentals of blockchain.
    2. Implement a Proof of Work (PoW) mechanism.
    3. Manage transactions with public/private keys and digital signatures.
    4. Simulate a network of miners validating transactions.

## Step 1: Build a Basic Blockchain
    1. Create a Block class that includes a hash and a reference to the previous block.
    2. Create a Blockchain class to store blocks.
    3. Add blocks with simple data.


## Step 2: Implement Proof of Work (PoW)
    1. Modify Block to include a nonce.
    2. Change calculate_hash() so the hash meets a difficulty target (e.g., starts with "0000").

## Step 3: Mining and Validating transactions
    1. Add a pending transactions pool in Blockchain.
    2. Modify mining to include transactions in a block.
    3. Reward the miner with a special transaction.
