# Autonomous Mission

---

## Process

1. **Get Frame from ROS Node**: Capture a frame from the camera feed via ROS.
2. **Detect Arrow/Cone**: Identify if an arrow or cone is present in the frame.
3. **Calculate Distance**: Measure the distance from the rover to the detected arrow or cone.
4. **Decision-Making**:
   - If `Distance < 0.7 meters`, stop for 10 seconds.
   - If an arrow is detected, **turn**; if a cone is detected, **stop** and **break**.
5. **Move Forward**: Continue moving forward if no action is taken.
6. **Loop**: Repeat this process in an infinite loop.

---

## To-Do List

- [ ] Implement the `RecieveImage` class to handle receiving images from the ROS node.
- [ ] Create a function to `Detect Arrow/Cone`.
- [ ] Develop a function to `Get Point and Distance` for the detected object.

---

## File Structure and Components

### Functions

- **Object Detection**
  - `detect_object()`: Detects an arrow or cone in the frame.
  - `get_point()`: Retrieves the coordinates of the detected object.
  - `get_distance()`: Calculates the distance to the detected object.

### Classes

#### ROS Node

- **Methods**
  - `subscriber()`: Subscribes to the camera feed.
  - `get_depth()`: Retrieves the depth at a given point.

- **Data**
  - `img`: Stores the captured image.
  - `depth`: Stores the depth information.
