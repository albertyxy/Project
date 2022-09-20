// Generated by gencpp from file V2X_Integration/SARA_06_Msg.msg
// DO NOT EDIT!


#ifndef V2X_INTEGRATION_MESSAGE_SARA_06_MSG_H
#define V2X_INTEGRATION_MESSAGE_SARA_06_MSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace V2X_Integration
{
template <class ContainerAllocator>
struct SARA_06_Msg_
{
  typedef SARA_06_Msg_<ContainerAllocator> Type;

  SARA_06_Msg_()
    : header()
    , SARA_06_CRC(0)
    , SARA_06_BZ(0)
    , SARA_Accel_X_010(0.0)
    , SARA_Accel_Y_010(0.0)
    , SARA_Omega_Z_010(0.0)
    , SARA_CF_Accel_X_010(0)
    , SARA_CF_Accel_Y_010(0)
    , SARA_CF_Omega_Z_010(0)  {
    }
  SARA_06_Msg_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , SARA_06_CRC(0)
    , SARA_06_BZ(0)
    , SARA_Accel_X_010(0.0)
    , SARA_Accel_Y_010(0.0)
    , SARA_Omega_Z_010(0.0)
    , SARA_CF_Accel_X_010(0)
    , SARA_CF_Accel_Y_010(0)
    , SARA_CF_Omega_Z_010(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint16_t _SARA_06_CRC_type;
  _SARA_06_CRC_type SARA_06_CRC;

   typedef uint8_t _SARA_06_BZ_type;
  _SARA_06_BZ_type SARA_06_BZ;

   typedef float _SARA_Accel_X_010_type;
  _SARA_Accel_X_010_type SARA_Accel_X_010;

   typedef float _SARA_Accel_Y_010_type;
  _SARA_Accel_Y_010_type SARA_Accel_Y_010;

   typedef float _SARA_Omega_Z_010_type;
  _SARA_Omega_Z_010_type SARA_Omega_Z_010;

   typedef uint8_t _SARA_CF_Accel_X_010_type;
  _SARA_CF_Accel_X_010_type SARA_CF_Accel_X_010;

   typedef uint8_t _SARA_CF_Accel_Y_010_type;
  _SARA_CF_Accel_Y_010_type SARA_CF_Accel_Y_010;

   typedef uint8_t _SARA_CF_Omega_Z_010_type;
  _SARA_CF_Omega_Z_010_type SARA_CF_Omega_Z_010;





  typedef boost::shared_ptr< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> const> ConstPtr;

}; // struct SARA_06_Msg_

typedef ::V2X_Integration::SARA_06_Msg_<std::allocator<void> > SARA_06_Msg;

typedef boost::shared_ptr< ::V2X_Integration::SARA_06_Msg > SARA_06_MsgPtr;
typedef boost::shared_ptr< ::V2X_Integration::SARA_06_Msg const> SARA_06_MsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::V2X_Integration::SARA_06_Msg_<ContainerAllocator1> & lhs, const ::V2X_Integration::SARA_06_Msg_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.SARA_06_CRC == rhs.SARA_06_CRC &&
    lhs.SARA_06_BZ == rhs.SARA_06_BZ &&
    lhs.SARA_Accel_X_010 == rhs.SARA_Accel_X_010 &&
    lhs.SARA_Accel_Y_010 == rhs.SARA_Accel_Y_010 &&
    lhs.SARA_Omega_Z_010 == rhs.SARA_Omega_Z_010 &&
    lhs.SARA_CF_Accel_X_010 == rhs.SARA_CF_Accel_X_010 &&
    lhs.SARA_CF_Accel_Y_010 == rhs.SARA_CF_Accel_Y_010 &&
    lhs.SARA_CF_Omega_Z_010 == rhs.SARA_CF_Omega_Z_010;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::V2X_Integration::SARA_06_Msg_<ContainerAllocator1> & lhs, const ::V2X_Integration::SARA_06_Msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace V2X_Integration

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2d6f91f1b10aaef29935d4bdfc80abae";
  }

  static const char* value(const ::V2X_Integration::SARA_06_Msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2d6f91f1b10aaef2ULL;
  static const uint64_t static_value2 = 0x9935d4bdfc80abaeULL;
};

template<class ContainerAllocator>
struct DataType< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "V2X_Integration/SARA_06_Msg";
  }

  static const char* value(const ::V2X_Integration::SARA_06_Msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"uint16 SARA_06_CRC\n"
"uint8 SARA_06_BZ\n"
"float32 SARA_Accel_X_010\n"
"float32 SARA_Accel_Y_010\n"
"float32 SARA_Omega_Z_010\n"
"uint8 SARA_CF_Accel_X_010\n"
"uint8 SARA_CF_Accel_Y_010\n"
"uint8 SARA_CF_Omega_Z_010\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::V2X_Integration::SARA_06_Msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.SARA_06_CRC);
      stream.next(m.SARA_06_BZ);
      stream.next(m.SARA_Accel_X_010);
      stream.next(m.SARA_Accel_Y_010);
      stream.next(m.SARA_Omega_Z_010);
      stream.next(m.SARA_CF_Accel_X_010);
      stream.next(m.SARA_CF_Accel_Y_010);
      stream.next(m.SARA_CF_Omega_Z_010);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SARA_06_Msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::V2X_Integration::SARA_06_Msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::V2X_Integration::SARA_06_Msg_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "SARA_06_CRC: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.SARA_06_CRC);
    s << indent << "SARA_06_BZ: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.SARA_06_BZ);
    s << indent << "SARA_Accel_X_010: ";
    Printer<float>::stream(s, indent + "  ", v.SARA_Accel_X_010);
    s << indent << "SARA_Accel_Y_010: ";
    Printer<float>::stream(s, indent + "  ", v.SARA_Accel_Y_010);
    s << indent << "SARA_Omega_Z_010: ";
    Printer<float>::stream(s, indent + "  ", v.SARA_Omega_Z_010);
    s << indent << "SARA_CF_Accel_X_010: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.SARA_CF_Accel_X_010);
    s << indent << "SARA_CF_Accel_Y_010: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.SARA_CF_Accel_Y_010);
    s << indent << "SARA_CF_Omega_Z_010: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.SARA_CF_Omega_Z_010);
  }
};

} // namespace message_operations
} // namespace ros

#endif // V2X_INTEGRATION_MESSAGE_SARA_06_MSG_H
