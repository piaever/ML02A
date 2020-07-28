{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4]\n",
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "a = np.array ([1,2,3,4])\n",
    "print(a)\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "a = [1,2,3,4]    # 리스트\n",
    "b = [1,2,3,4]\n",
    "\n",
    "print(a +b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 4 6 8]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1,2,3,4])     # 1차원 배열, 2차원 행렬, 3차원이상 텐서\n",
    "b = np.array([1,2,3,4]) \n",
    "\n",
    "print(a + b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1.4 2.4 3.3 4.2]\n",
      "[0.6 1.6 2.7 3.8]\n",
      "[0.4 0.8 0.9 0.8]\n",
      "[ 2.5  5.  10.  20. ]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1,2,3,4])     # 1차원 배열, 2차원 행렬, 3차원이상 텐서\n",
    "b = np.array([.4, .4, .3, .2])\n",
    "\n",
    "print(a + b)\n",
    "print(a - b)\n",
    "print(a * b)\n",
    "print(a / b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "A = np.array([[1], []])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
