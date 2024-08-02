<h1 align="center">🎵 Mood Tracks</h1>

<h2 align="center"> Song Sentiment Prediction Model</h2>

<h3> 📘 INTRO</h3>

<p>With the proliferation of machine learning and deep learning in content consumption, we are faced with an overwhelming amount of choices. <br>
  This often complicates decision-making rather than simplifying it. <br>
  For instance, deciding which movie to watch on Netflix or which song to listen to on Spotify.
</p>
<br>
<h3>📙 OPPORTUNITY</h3>
<p>Most recommendation systems track users' consumption patterns and suggest content based on their history. <br>
  While this approach indirectly reflects personality, mood and individual preferences, it fails to capture the consumer's current emotional state or live sentiment.
</p>
<br>
<h3>📗 SOLUTION</h3>
<p>We built a song sentiment prediction model which comes together on our app Mood Tracks and suggests music to consumers based on their real-time sentiment.</p>
<br>
<h3>📊 DATASETS</h3>
<table>
  <tr>
    <th>DATABASES</th>
    <th>LINK</th>
  </tr>
  <tr>
    <td>Kaggle Twitter Data 🦜</td>
    <td><a align="center" href="https://www.kaggle.com/datasets/kazanova/sentiment140">Here</a></td>
  </tr>
  <tr>
    <td>Spotify Tracks Dataset 🎧</td>
    <td><a align="center" href="https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset">Here</a></td>
  </tr>
    <tr>
    <td>Genius Song Lyrics 🎵</td>
    <td><a align="center" href="https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information">Here</a></td>
  </tr>
</table>
<br>
<h3>🔐 API</h3>
<table>
  <tr>
    <th>API</th>
    <th>LINK</th>
  </tr>
  <tr>
    <td>Spotify API 🎧</td>
    <td><a align="center" href="https://developer.spotify.com/documentation/web-api">Here</a></td>
  </tr>
</table>
<br>
<h3>🤖 MODELS</h3>
<ul>
  <li><b>Latent Dirichlet Allocation (LDA)</b> - First we implemented an LDA model and trained it on X/Twitter data to identify 40 distinct topics, which we use to classify user input.
</li>
  <br>
  <li><b>Roberta (Hugging Face)</b> <em>cardiffnlp/twitter-roberta-base-sentiment-latest</em> - We then used state-of-the-art models from Hugging Face to analyze the sentiment of both user inputs and song lyrics, classifying them into negative, neutral, or positive sentiments.
</li>
  <br>
  <li><b>K-Means</b> - We employed K-Means clustering on Spotify data, which includes features like loudness and energy, to group songs into three emotional categories matching the sentiment from our Hugging Face model.
  </li>
</ul>
<br>

<h3>🌊 USER FLOW</h3>

<div style="text-align: center;">

<p><strong>1. User Input</strong> - Message and checks a checkbox</p>
<p>⬇️</p>

<p><strong>2. Backend</strong> - Models search for songs that match topics</p>
<p>⬇️</p>

<p><strong>3. Backend</strong> - Based on the selection, the model generates recommendations</p>
<p>⬇️</p>

<p><strong>4. Outputs</strong> - Displays playable songs</p>
<p>🔄 <strong>Randomize</strong> ⬆️ (circles back to point 2)</p>

</div>

<h4>🌊 USER OPTIONS CATEGORIES </h4>
<ul>
    <li>😢 Lyrics are matched to user sentiment & topics, with random sound</li>
    <li>😁 Lyrics are matched to topics, but lyrics and sounds are positive</li>
    <li>🙃 Topics are not matched but songs have positive lyrics & sound</li>
</ul>



<h1 align="center">🥳 FINAL OUTPUT</h1>
<p align="center">➡️ left to right</p>
<div style="display: flex; justify-content: space-around;">
  <a href="https://github.com/user-attachments/assets/95dba204-a464-4b64-9468-905d4062c052">
    <img src="https://github.com/user-attachments/assets/95dba204-a464-4b64-9468-905d4062c052" alt="Image 1" style="width: 30%;">
  </a>
  <a href="https://github.com/user-attachments/assets/92338da8-6a6c-4e70-b0fb-e872d57de06d">
    <img src="https://github.com/user-attachments/assets/92338da8-6a6c-4e70-b0fb-e872d57de06d" alt="Image 2" style="width: 30%;">
  </a>
  <a href="https://github.com/user-attachments/assets/c66e1dfc-c73a-46de-8bd0-f16da3cee288">
    <img src="https://github.com/user-attachments/assets/c66e1dfc-c73a-46de-8bd0-f16da3cee288" alt="Image 3" style="width: 30%;">
  </a>
</div>
