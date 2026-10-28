{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMVWIybLwI0fLVqZd9pcR36",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/HanyunJiang/llm-learning-log/blob/main/day01.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "def add_all(numbers):\n",
        "  total=0\n",
        "  for n in numbers:\n",
        "    total=toal+n\n",
        "    return total\n",
        "def is_even(n):\n",
        "  if n%2==0:\n",
        "    return True\n",
        "  else:\n",
        "      return False\n",
        "\n",
        "def word_count(text):\n",
        "  counts={}\n",
        "  words=text.split()\n",
        "  for w in words:\n",
        "    if w in counts:\n",
        "      counts[w]+=1\n",
        "    else:\n",
        "      counts[w]=1\n",
        "      return counts\n",
        "#测试\n",
        "nums=[3,7,10,2,8]\n",
        "print(\"求和：\",add_all(nums))\n",
        "print(\"10是偶数吗：\",is_even(10))\n",
        "print(\"7是偶数吗\",is_even(7))\n",
        "print(\"词频：\",word_count(\"cat dog cat bird dog cat\"))\n",
        "\n",
        "\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VUB1wV-4loxT",
        "outputId": "b0eda178-f11a-4715-8420-92bb42b555c7"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting day2.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!python day2.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DHjUhEBNqtV0",
        "outputId": "b69c6fe4-27dd-4d67-c90e-9f0fc89afab2"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "求和： 30\n",
            "10是偶数吗： True\n",
            "7是偶数吗： False\n",
            "词频： {'cat': 3, 'dog': 2, 'bird': 1}\n"
          ]
        }
      ]
    }
  ]
}