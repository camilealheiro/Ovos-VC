#####################################################
##               Read bag from file                ##
#####################################################


# First import library
import pyrealsense2 as rs
# Import Numpy for easy array manipulation
import numpy as np
# Import OpenCV for easy image rendering
import cv2
# Import argparse for command-line options
import argparse
# Import os.path for file path manipulation
import os.path

def get_depth_at_pixel(depth_frame, pixel_x, pixel_y):
	"""
	Get the depth value at the desired image point

	Parameters:
	-----------
	depth_frame 	 : rs.frame()
						   The depth frame containing the depth information of the image coordinate
	pixel_x 	  	 	 : double
						   The x value of the image coordinate
	pixel_y 	  	 	 : double
							The y value of the image coordinate

	Return:
	----------
	depth value at the desired pixel

	"""
	return depth_frame.as_depth_frame().get_distance(round(pixel_x), round(pixel_y))

# Create object for parsing command-line options
parser = argparse.ArgumentParser(description="Read recorded bag file and display depth stream in jet colormap.\
                                Remember to change the stream fps and format to match the recorded.")
# Add argument which takes path to a bag file as an input
parser.add_argument("-i", "--input", type=str, help="Path to the bag file")
# Parse the command line arguments to an object
args = parser.parse_args()
# Safety if no parameter have been given
if not args.input:
    print("No input paramater have been given.")
    print("For help type --help")
    exit()
# Check if the given file have bag extension
if os.path.splitext(args.input)[1] != ".bag":
    print("The given file is not of correct file format.")
    print("Only .bag files are accepted")
    exit()
try:
    # Create pipeline
    pipeline = rs.pipeline()

    # Create a config object
    config = rs.config()

    # Tell config that we will use a recorded device from file to be used by the pipeline through playback.
    rs.config.enable_device_from_file(config, args.input)

    # Configure the pipeline to stream the depth stream
    # Change this parameters according to the recorded bag file resolution
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)

    # Start streaming from file
    pipeline.start(config)

    # Create opencv window to render image in
    cv2.namedWindow("Depth Stream", cv2.WINDOW_AUTOSIZE)
    
    # Create colorizer object
    colorizer = rs.colorizer()

    frame = pipeline.wait_for_frames()

    # Get depth frame
    depth_frames = frame.get_depth_frame()

    # Colorize depth frame to jet colormap
    depth_color_frame = colorizer.colorize(depth_frames)

    # Convert depth_frame to numpy array to render image in opencv
    depth_image = np.asarray(depth_frames.get_data(), dtype=np.uint16)
    #cv2.imwrite("dept.png", depth_image)

    norm = []
    def normalize_list(input_list):
        # Encontrar os valores mínimo e máximo na lista original
        min_val = 350
        max_val = 3000

        # Normalizar os valores na lista para o intervalo [0, 1]
        for x in input_list:
             conv = (x - min_val) / (max_val - min_val)
             norm.append(conv)

        return norm
    

    IMAGE_WIDTH = 640
    IMAGE_HEIGHT = 480
    framesize = IMAGE_WIDTH * IMAGE_HEIGHT
    
    teste = []
    for y in range(480):
        for x in range(640):
            valor = get_depth_at_pixel(depth_frame=depth_frames, pixel_x=x, pixel_y=y)

            if valor > 3:
                 valor = 3
                 teste.append(valor)
            else:
                teste.append(valor)

    array = np.asanyarray(teste, dtype=np.double)
    array *= 10000
    array16 = array.astype(np.uint16)

    
    reshape = np.reshape(array16, (IMAGE_HEIGHT, IMAGE_WIDTH))
    

    cv2.imwrite("multi3000.png", reshape)
    #print(teste)
    #print(reshape)

    # # Streaming loop
    # while True:
    #     # Get frameset of depth
    #     frames = pipeline.wait_for_frames()

    #     # Get depth frame
    #     depth_frame = frames.get_depth_frame()

    #     # Colorize depth frame to jet colormap
    #     depth_color_frame = colorizer.colorize(depth_frame)

    #     # Convert depth_frame to numpy array to render image in opencv
    #     depth_color_image = np.asanyarray(depth_color_frame.get_data())
    #     #depth_image = np.asarray(depth_frame.get_data(), dtype=np.uint16)

    #     #valor = get_depth_at_pixel(depth_frame=depth_frame, pixel_x=110, pixel_y=100)
    #     #print(valor)

    #     #depth_color_image_16bits = np.array(depth_frame, dtype=np.uint16)
    #     #depth_color_image_16bits *= 256

    #     #resized = cv2.resize(depth_color_image_16bits, (640, 480), interpolation=cv2.INTER_AREA)
    #     #cv2.imwrite("depth.png", depth_image)

    #     # Render image in opencv window
    #     cv2.imshow("Depth Stream", depth_color_image)
    #     key = cv2.waitKey(1)

    #     # if pressed escape exit program

    #     if key == 27:
    #         cv2.destroyAllWindows()
    #         break


finally:
    pass