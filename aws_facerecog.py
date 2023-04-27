# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier:
# MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def compare_faces(sourcefile, target_file):

    print("------ Lests compare faces using AWS -------")

    client = boto3.client('rekognition')

    imagesource = open(sourcefile, 'rb')
    print('Loaded:', sourcefile)
    image_target = open(target_file, 'rb')
    print('Loaded:', target_file)

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imagesource.read()},
                                    TargetImage={'Bytes': image_target.read()})
    print(response)

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + similarity + '% confidence')

    imagesource.close()
    image_target.close()
    return len(response['FaceMatches'])


def main():
    source_file = 'CNH.jpeg'
    target_file1 = 'Executive.png'
    #target_file1 = 'tom.png'
    face_matches = compare_faces(source_file, target_file1)
    print("Face matches: " + str(face_matches))


if __name__ == "__main__":
    main()