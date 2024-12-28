{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3979f47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://0.0.0.0:5555/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def hello_world():\n",
    "    return 'Hello, World!'\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(host=\"0.0.0.0\", port=5555)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9c481ea",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
