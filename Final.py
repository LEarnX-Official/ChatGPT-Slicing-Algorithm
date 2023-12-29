import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()

    words = nltk.word_tokenize(text)
    words = [ps.stem(word) for word in words if word.isalnum() and word.lower() not in stop_words]

    return ' '.join(words)

def generate_slices(input_text, max_size=128):
    slices = []
    text_length = len(input_text)

    if text_length > max_size * 1024:  # Check if the input size is above the standard size (128 MB)
        # If the input is above the standard size, generate slices
        target_size = max_size * 1024
        start = 0

        while start < text_length:
            end = min(start + target_size, text_length)
            slice_text = input_text[start:end]
            slices.append(slice_text)

            # Allow overlapping slices
            start += target_size // 2

    return slices

def cosine_distance(slice1, slice2):
    vectorizer = CountVectorizer().fit_transform([slice1, slice2])
    vectors = vectorizer.toarray()
    return cosine_similarity([vectors[0]], [vectors[1]])[0][0]

def find_disjoint_slices(slices, threshold=0.2):
    if not slices:
        return []

    result_slices = [slices[0]]

    for i in range(1, len(slices)):
        is_disjoint = True

        for existing_slice in result_slices:
            distance = cosine_distance(existing_slice, slices[i])

            if distance < threshold:
                is_disjoint = False
                break

        if is_disjoint:
            result_slices.append(slices[i])

    return result_slices

# Take input file path from the user
file_path = input("Enter the path to your text file: ")

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Preprocess the text
preprocessed_input = preprocess_text(input_text)

# Generate slices and find disjoint slices
slices = generate_slices(preprocessed_input)
disjoint_slices = find_disjoint_slices(slices)

# Print the result
for i, slice_text in enumerate(disjoint_slices):
    print(f"Slice {i+1}:\n{slice_text}\n")

