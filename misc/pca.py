import sqlite3
import numpy as np
from scipy import stats
import sklearn.decomposition
import matplotlib.pyplot as plt

num_to_alpha = ['Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia',
                "Cho'Gath", 'Corki', 'Darius', 'Diana', 'Draven', 'Dr. Mundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar',
                'Gragas', 'Graves', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'Sa", 'Kalista', 'Karma', 'Karthus', 'Kassadin',
                'Katarina', 'Kayle', 'Kayn', 'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", 'LeBlanc', 'Lee Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar',
                'Maokai', 'Master Yi', 'Miss Fortune', 'Wukong', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon',
                'Poppy', 'Pyke', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner',
                'Sona', 'Soraka', 'Swain', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot',
                'Varus', 'Vayne', 'Veigar', "Vel'Koz", 'Vi', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']

# We load the champs median and standard deviation data
db = sqlite3.connect("CHAMPS.db")
raw = np.array(db.execute("SELECT * FROM data").fetchall()).T[1:].T
##raw = np.array(db.execute("SELECT * FROM data").fetchall()).T[7:].T

print(raw)

# First we will calculate the z-scores for all the variables (obtaining a normal distribution)
zscores = stats.zscore(raw, axis=0)

# Execute PCA and reduce to 2D
pca = sklearn.decomposition.PCA(n_components=43)
pca.fit(zscores)

# 2D PLOTTING

## Get the 2D representation
##repre = np.dot(zscores, pca.components_.T)
##repreT = repre.T
##
##for champ in range(len(repre)):
##    print(str(repre[champ])+" "+str(num_to_alpha[champ]))
##
## Plot the results
##plt.plot(repreT[0], repreT[1], 'ro')
##
##for i, txt in enumerate(num_to_alpha):
##    plt.annotate(txt, (repreT[0][i],repreT[1][i]))
##
##plt.show()


# VARIANCE PRESERVATION PLOT

relevance = pca.singular_values_/pca.singular_values_.sum()
cumrelevance  = [relevance[:i+1].sum() for i in range(len(relevance))]

print(cumrelevance)

plt.plot(range(len(cumrelevance)), cumrelevance, 'bo', range(len(cumrelevance)), cumrelevance, 'k', range(len(relevance)), relevance, 'ro', range(len(relevance)), relevance, 'k',)
plt.show()
