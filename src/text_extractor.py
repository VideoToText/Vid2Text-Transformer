import io
import logging
from google.cloud import videointelligence

def extract_text_from_video(video_path):
    """
    Using Google Vision API or other OCR tools, extract text from video.
    """

    """Detect text in a local video."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.TEXT_DETECTION]
    video_context = videointelligence.VideoContext()

    count = 0
    with io.open(video_path, "rb") as file:
        input_content = file.read()

    logging.basicConfig(level=logging.INFO)

    try:
        logging.info("API call started")
        operation = video_client.annotate_video(
            request={
                "features": features,
                "input_content": input_content,
                "video_context": video_context,
            }
        )
        logging.info("API call finished")
    except Exception as e:
        logging.error(f"API call failed: {str(e)}")

    print("\nProcessing video for text detection.")
    result = operation.result(timeout=300)

    # The first result is retrieved because a single video was processed.
    annotation_result = result.annotation_results[0]
    text = ""
    print(annotation_result)
    for text_annotation in annotation_result.text_annotations:
        print("\nText: {}".format(text_annotation.text))
        text += text_annotation.text + "\n"

        # Get the first text segment
        text_segment = text_annotation.segments[0]
        start_time = text_segment.segment.start_time_offset
        end_time = text_segment.segment.end_time_offset
        print(
            "start_time: {}, end_time: {}".format(
                start_time.seconds + start_time.microseconds * 1e-6,
                end_time.seconds + end_time.microseconds * 1e-6,
            )
        )

        print("Confidence: {}".format(text_segment.confidence))

        # Show the result for the first frame in this segment.
        frame = text_segment.frames[0]
        time_offset = frame.time_offset
        print(
            "Time offset for the first frame: {}".format(
                time_offset.seconds + time_offset.microseconds * 1e-6
            )
        )
        print("Rotated Bounding Box Vertices:")
        for vertex in frame.rotated_bounding_box.vertices:
            print("\tVertex.x: {}, Vertex.y: {}".format(vertex.x, vertex.y))
    return text

# print(extract_text_from_video("./sample.mp4"))