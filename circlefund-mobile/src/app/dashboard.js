import { View, Text } from "react-native";

export default function Dashboard() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text
        style={{
          fontSize: 30,
          fontWeight: "bold",
        }}
      >
        User Tets Dashboard....
      </Text>
    </View>
  );
}